# API Versioning Strategies
#
# URL Versioning:
# /api/v1/courses/
#
# Header Versioning:
# Accept: application/vnd.api+json;version=1
#
# URL versioning is simpler and easier to test.
# Header versioning keeps URLs cleaner.

from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from sqlalchemy import or_

from database import engine
from database import get_db

from models import Base,Course,User
from security import get_password_hash
from jose import JWTError, jwt

from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
    UserCreate,
    UserResponse,
    LoginRequest,
    Token
)
from security import (
    verify_password,
    create_access_token,
    SECRET_KEY,
    ALGORITHM
)

app = FastAPI(
    title="Course Management API",
    description="Course Management API with REST Best Practices",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

Base.metadata.create_all(bind=engine)

#----------------------------------------
# OAuth2PasswordBearer instance
#----------------------------------------

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login/"
)

#----------------------------------------
# Dependency to get current user
#----------------------------------------

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user

# ----------------------------------------
# Standardized Error Response
# ----------------------------------------
def error_response(
    code: str,
    message: str,
    field=None
):
    return {
        "error": {
            "code": code,
            "message": message,
            "field": field
        }
    }


# ----------------------------------------
# Home Endpoint
# ----------------------------------------
@app.get("/")
def home():
    return {
        "message": "Database Connected"
    }
    

# ----------------------------------------
# Create Course
# ----------------------------------------

@app.post(
    "/api/v1/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED
)

def create_course(
    course: CourseCreate,
    response: Response,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    db_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    response.headers["Location"] = (
        f"/api/v1/courses/{db_course.id}"
    )

    return db_course


# ----------------------------------------
# Get All Courses
# Pagination + Search
# ----------------------------------------
@app.get("/api/v1/courses/")
def get_courses(
    page: int = 1,
    page_size: int = 2,
    search: str | None = None,
    db: Session = Depends(get_db)
):

    query = db.query(Course)

    if search:
        query = query.filter(
            or_(
                Course.name.ilike(f"%{search}%"),
                Course.code.ilike(f"%{search}%")
            )
        )

    total = query.count()

    offset = (page - 1) * page_size

    courses = (
        query
        .offset(offset)
        .limit(page_size)
        .all()
    )

    next_url = None
    previous_url = None

    if offset + page_size < total:
        next_url = (
            f"/api/v1/courses/?page={page+1}&page_size={page_size}"
        )

    if page > 1:
        previous_url = (
            f"/api/v1/courses/?page={page-1}&page_size={page_size}"
        )

    return {
        "count": total,
        "next": next_url,
        "previous": previous_url,
        "results": courses
    }


# ----------------------------------------
# Get Course By ID
# ----------------------------------------
@app.get(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse
)
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):

    course = (
        db.query(Course)
        .filter(Course.id == course_id)
        .first()
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail=error_response(
                "NOT_FOUND",
                f"Course with id {course_id} does not exist"
            )
        )

    return course


# ----------------------------------------
# Update Course (PUT)
# ----------------------------------------
@app.put(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse
)
def update_course(
    course_id: int,
    course_update: CourseUpdate,
    db: Session = Depends(get_db)
):

    course = (
        db.query(Course)
        .filter(Course.id == course_id)
        .first()
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail=error_response(
                "NOT_FOUND",
                f"Course with id {course_id} does not exist"
            )
        )

    update_data = course_update.model_dump()

    for key, value in update_data.items():
        setattr(course, key, value)

    db.commit()
    db.refresh(course)

    return course


# ----------------------------------------
# Partial Update (PATCH)
# ----------------------------------------
@app.patch(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse
)
def patch_course(
    course_id: int,
    course_update: CourseUpdate,
    db: Session = Depends(get_db)
):

    course = (
        db.query(Course)
        .filter(Course.id == course_id)
        .first()
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail=error_response(
                "NOT_FOUND",
                f"Course with id {course_id} does not exist"
            )
        )

    update_data = course_update.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(course, key, value)

    db.commit()
    db.refresh(course)

    return course


# ----------------------------------------
# Delete Course
# ----------------------------------------
@app.delete(
    "/api/v1/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_course(
    course_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    course = (
        db.query(Course)
        .filter(Course.id == course_id)
        .first()
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail=error_response(
                "NOT_FOUND",
                f"Course with id {course_id} does not exist"
            )
        )

    db.delete(course)
    db.commit()

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )
    
# ----------------------------------------
# User Registration Endpoint
# ----------------------------------------

@app.post(
    "/api/v1/auth/register/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    hashed_password = (
        get_password_hash(
            user.password
        )
    )

    new_user = User(
        email=user.email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# ----------------------------------------
# Login Endpoint
# ----------------------------------------

@app.post(
    "/api/v1/auth/login/",
    response_model=Token
)
def login_user(
    user_credentials: LoginRequest,
    db: Session = Depends(get_db)
):

    # Find user by email
    user = (
        db.query(User)
        .filter(
            User.email ==
            user_credentials.email
        )
        .first()
    )

    # Check whether user exists
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    # Verify password
    if not verify_password(
        user_credentials.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    # Generate JWT token
    access_token = create_access_token(
        {
            "sub": user.email
        }
    )

    # Return token
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
    
