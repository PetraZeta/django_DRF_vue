import axiosClient from "./axiosClient"

const userService = {
  getAllUsers() {
    return axiosClient.get("/users");
  },

  getUserById(id) {
    return axiosClient.get(`/users/${id}`);
  },

  createUser(userData) {
    return axiosClient.post("/users", userData);
  },

  updateUser(id, updatedUserData) {
    return axiosClient.put(`/users/${id}`, updatedUserData);
  },

  deleteUser(id) {
    return axiosClient.delete(`/users/${id}`);
  }
};

export default userService;
