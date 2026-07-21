import { defineStore } from "pinia";
import { getAllCourses, enrollStudent } from "../api/courseApi";

export const useCourseStore =
    defineStore("courses", {

        state: () => ({

            courses: [],

            loading: false,

            error: null

        }),

        actions: {

            async fetchCourses() {

                this.loading = true;

                this.error = null;

                try {

                    this.courses =
                        await getAllCourses();

                }

                catch (err) {

                    this.error =
                        err.message;

                }

                finally {

                    this.loading = false;

                }

            },

            async fetchAndEnroll(courseId) {

                try {

                    await enrollStudent(
                        101,
                        courseId
                    );

                    alert(
                        `Successfully enrolled in course ${courseId}`
                    );

                }

                catch (error) {

                    this.error =
                        error.message;

                }

            },

            resetStore() {

                this.$reset();

            }

        }

    });