import axios from 'axios'

export const getCourses = () => {

    return axios.get(
        'https://jsonplaceholder.typicode.com/posts?_limit=5'
    )

}