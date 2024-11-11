<script>
import axios from "axios";
import { useStore } from "../stores/store.js";
import router from "../router";

export default {
  data() {
    return {

      store: useStore(),

      manager_username: null,
      manager_password: null,
      manager_buildings: [],

      user_for_delete: null,

    };
  },

  async mounted() {
    await this.store.getBuildings();
    await this.store.getUsers();
  },

  computed: {
    // Computed property to filter users with the "inhabitant" role
    managers() {
      return this.store.users.filter(user => user.role === "manager");
    },
  },

  methods: {
    async submitManagerForm() {

      const manager = {
        username: this.manager_username,
        password: this.manager_password,
        buildings: this.manager_buildings,
      };

      try {
        await axios.post("http://localhost:8000/backend/api/add_manager/", manager, {
          headers: {
            "Content-Type": "application/json",
          },
        });
      
      this.store.getUsers();
      } catch (error) {
        console.error("Error creating manager:", error);
        alert("Failed to create manager.");
      }
    },

    async deleteUser() {
    try {
      const response = await axios.delete(`http://localhost:8000/backend/api/delete_user/${this.user_for_delete}/`, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      this.store.getUsers();
    } catch (error) {
      console.error("Error deleting user:", error);
      alert("Failed to delete user.");
    }
  },
  },
};
</script>

<template>
<div class="manage-users">

  <h1>Manage Manager</h1>

  <div class="create-manager-page">
    <h2>Create Manager</h2>
    <form @submit.prevent="submitManagerForm" class="manager-form">
      <!-- Username Field -->
      <div class="form-group">
        <label for="username">Username:</label><br>
        <input v-model="this.manager_username" type="text" id="manager_username" required />
      </div>

      <!-- Password Field -->
      <div class="form-group">
        <label for="password">Password:</label><br>
        <input v-model="this.manager_password" type="password" id="manager_password" required />
      </div>

      <!-- Buildings Multi-Select Dropdown -->
      <div class="form-group">
        <label for="buildings">Buildings:</label><br>
        <select v-model="this.manager_buildings" id="manager_buildings" multiple>
          <option v-for="building in this.store.buildings" :key="building.id" :value="building.id">
            {{ building.address }} - {{ building.number }}
          </option>
        </select>
      </div>

      <!-- Submit Button -->
      <button type="submit" class="btn btn-primary">Add Manager</button>
    </form>
  </div>

  <div class="delete-user">
    <h2>Manager Deleting</h2>

    <ul>
      <label for="userSelect">Select User:</label><br>
      <select v-model="this.user_for_delete" id="userSelect">
        <option disabled value="">Select a User</option>
        <option v-for="user in managers" :key="user.id" :value="user.id">
          {{ user.username }} - {{ user.role }}
        </option>
      </select>    
    </ul>

    <button @click="deleteUser" class="btn btn-danger" :disabled="!this.user_for_delete">
      Delete User
    </button>
  </div>
</div>

</template>