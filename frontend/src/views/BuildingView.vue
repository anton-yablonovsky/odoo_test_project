<script>
import axios from "axios";
import { useStore } from "../stores/store.js";
import router from "../router";

export default {
  data() {
    return {
      store: useStore(),

      building_address: null,
      building_number: null,
      building_for_delete: null,
    };
  },

  async mounted() {
    await this.store.getBuildings();
  },

  methods: {
    async submitBuildingForm() {
      const formData = {
        address: this.building_address,
        number: this.building_number,
      };

      try {
        await axios.post(
          "http://localhost:8000/backend/api/add_building/",
          formData,
          {
            headers: {
              "Content-Type": "application/json",
            },
          },
        );

        await this.store.getBuildings();
      } catch (error) {
        console.error("Error creating building:", error);
        alert("Failed to create building.");
      }
    },

    async deleteBuildingForm() {
      if (!this.building_for_delete) {
        alert("Please select a building to delete.");
        return;
      }

      try {
        await axios.delete(
          `http://localhost:8000/backend/api/delete_building/${this.building_for_delete}/`,
          {
            headers: {
              "Content-Type": "application/json",
            },
          },
        );

        await this.store.getBuildings();
      } catch (error) {
        console.error("Error deleting building:", error);
        alert("Failed to delete building.");
      }
    },
  },
};
</script>

<template>
  <div class="manage-buildings">
    <h1>Manage Building</h1>

    <div class="create-building-page">
      <h2>Create Building</h2>
      <form @submit.prevent="submitBuildingForm" class="building-form">
        <!-- Address Field -->
        <div class="form-group">
          <label for="address">Address:</label><br />
          <input
            v-model="this.building_address"
            type="text"
            id="building_address"
            required
          />
        </div>

        <!-- Number Field -->
        <div class="form-group">
          <label for="number">Number:</label><br />
          <input
            v-model="this.building_number"
            type="text"
            id="building_number"
            required
          />
        </div>

        <!-- Submit Button -->
        <button type="submit" class="btn btn-primary">Add Building</button>
      </form>
    </div>

    <div>
      <h2>Delete a Building</h2>
      <form @submit.prevent="deleteBuildingForm" class="delete-building-form">
        <div class="form-group">
          <label for="buildingSelect">Select Building to Delete:</label><br />
          <select
            v-model="this.building_for_delete"
            id="building_for_delete"
            required
          >
            <option value="" disabled>Select a Building</option>
            <option
              v-for="building in this.store.buildings"
              :key="building.id"
              :value="building.id"
            >
              {{ building.address }} - {{ building.number }}
            </option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">Delete Building</button>
      </form>
    </div>
  </div>
</template>
