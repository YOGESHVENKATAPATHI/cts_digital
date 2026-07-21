const courses = [
    {
        id: 1,
        name: "Data Structures",
        code: "CS101",
        credits: 4,
        grade: "A"
    },
    {
        id: 2,
        name: "Database Management",
        code: "CS102",
        credits: 3,
        grade: "A+"
    },
    {
        id: 3,
        name: "Web Development",
        code: "CS103",
        credits: 4,
        grade: "B+"
    },
    {
        id: 4,
        name: "Operating Systems",
        code: "CS104",
        credits: 4,
        grade: "A"
    },
    {
        id: 5,
        name: "Computer Networks",
        code: "CS105",
        credits: 3,
        grade: "B"
    }
];

const totalCreditsText =
    document.querySelector("#total-credits");

const searchInput =
    document.querySelector("#search-courses");

const sortButton =
    document.querySelector("#sort-btn");

const selectedCourse =
    document.querySelector("#selected-course");

const courseGrid =
    document.querySelector(".course-grid");

const loadingMessage =
    document.querySelector("#loading-message");

const notificationSection =
    document.querySelector(
        "#notification-section"
    );

const retryButton =
    document.querySelector(
        "#retry-btn"
    );

// Fetch User Data

function fetchUser(id) {

    return fetch(
        `https://jsonplaceholder.typicode.com/users/${id}`
    );

}

fetchUser(1)
    .then(response => response.json())
    .then(user => {

        console.log("Promise Version:");
        console.log(user.name);

    })
    .catch(error => {

        console.error(error);

    });

// Async/Await Version
async function fetchUserAsync(id) {

    try {

        const response =
            await fetch(
                `https://jsonplaceholder.typicode.com/users/${id}`
            );

        const user =
            await response.json();

        console.log("Async/Await Version:");
        console.log(user.name);

    }
    catch (error) {

        console.error(error);

    }

}

fetchUserAsync(1);

/* Render Courses */

function renderCourses(courseArray) {

    courseGrid.innerHTML = "";

    courseArray.forEach(course => {

        const article =
            document.createElement("article");

        article.className = "course-card";

        article.innerHTML = `
            <h3>${course.name}</h3>
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

renderCourses(courses);

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

        courses.sort(
            (a, b) =>
                b.credits - a.credits
        );

        renderCourses(courses);

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

function fetchAllCourses() {

    return new Promise((resolve) => {

        setTimeout(() => {

            resolve(courses);

        }, 1000);

    });

}

fetchAllCourses()
    .then(data => {

        loadingMessage.style.display = "none";

        renderCourses(data);

    });

Promise.all([

    fetch(
        "https://jsonplaceholder.typicode.com/users/1"
    ).then(response => response.json()),

    fetch(
        "https://jsonplaceholder.typicode.com/users/2"
    ).then(response => response.json())

])
    .then(users => {

        console.log("Promise.all Result:");

        console.log(users[0].name);

        console.log(users[1].name);

    })
    .catch(error => {

        console.error(error);

    });

// Async/Await with Error Handling 
async function apiFetch(url){

    try{

        loadingMessage.style.display =
            "block";

        const response =
            await fetch(url);

        if(!response.ok){

            throw new Error(
                "API Request Failed"
            );

        }

        return await response.json();

    }
    catch(error){

        console.error(error);

        throw error;

    }
    finally{

        loadingMessage.style.display =
            "none";

    }

}

// Render Notifications
function renderNotifications(data){

    notificationSection.innerHTML =
        "";

    data.slice(0,5)
        .forEach(notification => {

            const card =
                document.createElement(
                    "div"
                );

            card.className =
                "notification-card";

            card.innerHTML = `
                <h4>
                    ${notification.title}
                </h4>

                <p>
                    ${notification.body}
                </p>
            `;

            notificationSection
                .appendChild(card);

        });

}

// Load Notifications
async function loadNotifications(){

    try{

        const notifications =
            await apiFetch(
                "https://jsonplaceholder.typicode.com/posts"
            );

        renderNotifications(
            notifications
        );

    }
    catch(error){

        notificationSection.innerHTML = `
            <p>
                Failed to load notifications.
            </p>
        `;

    }

}

// Initial Load of Notifications
loadNotifications();

// Retry Button Event Listener
retryButton.addEventListener(
    "click",
    loadNotifications
);


//  Axios Integration

const apiClient = axios.create({

    baseURL:
        "https://jsonplaceholder.typicode.com",

    timeout: 5000

});

// Request Interceptor
apiClient.interceptors.request.use(
    config => {

        console.log(
            "Request Sent:",
            config.url
        );

        return config;

    },

    error => {

        return Promise.reject(error);

    }
);

// Response Interceptor
apiClient.interceptors.response.use(

    response => {

        console.log(
            "Response Received"
        );

        return response;

    },

    error => {

        console.error(
            "Axios Error:",
            error.message
        );

        return Promise.reject(error);

    }

);

// Fetch Posts using Axios
async function fetchPostsAxios(){

    try{

        const response =
            await apiClient.get(
                "/posts"
            );

        console.log(
            "Axios Posts Loaded"
        );

        console.log(
            response.data.slice(0,3)
        );

    }
    catch(error){

        console.error(error);

    }

}

// Initial Fetch of Posts using Axios
fetchPostsAxios();