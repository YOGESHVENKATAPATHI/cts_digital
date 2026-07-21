import { courses } from "./data.js";

let courseData = [...courses];

const courseGrid =
    document.querySelector(".course-grid");

const totalCreditsText =
    document.querySelector("#total-credits");

const searchInput =
    document.querySelector("#search-courses");

const sortButton =
    document.querySelector("#sort-btn");

const selectedCourse =
    document.querySelector("#selected-course");

/* Render Courses */

function renderCourses(courseArray) {

    courseGrid.innerHTML = "";

    courseArray.forEach(course => {

        const article =
            document.createElement("article");

        article.className =
            "course-card";

        article.dataset.id =
            course.id;

        article.innerHTML = `
            <h3>${course.name}</h3>
            <p>${course.code}</p>
            <p>${course.credits} Credits</p>
        `;

        courseGrid.appendChild(article);

    });

}

/* Total Credits */

const totalCredits =
    courses.reduce(
        (sum, course) =>
            sum + course.credits,
        0
    );

totalCreditsText.textContent =
    `Total Credits Enrolled: ${totalCredits}`;

/* Initial Render */

renderCourses(courseData);

/* Search */

searchInput.addEventListener(
    "input",
    (event) => {

        const searchTerm =
            event.target.value
                .toLowerCase();

        const filteredCourses =
            courses.filter(course =>
                course.name
                    .toLowerCase()
                    .includes(searchTerm)
            );

        renderCourses(filteredCourses);

    }
);

/* Sort */

sortButton.addEventListener(
    "click",
    () => {

        courseData.sort(
            (a, b) =>
                b.credits - a.credits
        );

        renderCourses(courseData);

    }
);

/* Event Delegation */

courseGrid.addEventListener(
    "click",
    (event) => {

        const card =
            event.target.closest(
                ".course-card"
            );

        if (!card) return;

        const courseId =
            Number(card.dataset.id);

        const course =
            courses.find(
                c => c.id === courseId
            );

        selectedCourse.innerHTML = `
            <h3>${course.name}</h3>
            <p>Code: ${course.code}</p>
            <p>Credits: ${course.credits}</p>
            <p>Grade: ${course.grade}</p>
        `;

    }
);