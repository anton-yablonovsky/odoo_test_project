<script>
import axios from "axios";
import { useStore } from "../stores/store.js";
import router from "../router";

export default {
  data() {
    return {

      store: useStore(),

      entrance_building: null,
      entrance_number: null,
      entrance_for_delete: null,

    };
  },

  async mounted() {
    await this.store.getEntrances();
  },

  methods: {
    async submitEntranceForm() {
        const formData = {
          building: this.entrance_building,
          number: this.entrance_number
        };

        try {
          await axios.post("http://localhost:8000/backend/api/add_entrance/", formData, {
            headers: {
              "Content-Type": "application/json",
            },
          });

        await this.store.getEntrances();

        } catch (error) {
          console.error("Error creating entrance:", error);
          alert("Failed to create entrance.");
        }
      },
    
    async deleteEntranceForm() {
      if (!this.entrance_for_delete) {
        alert("Please select an entrance to delete.");
        return;
      }

      try {
        await axios.delete(`http://localhost:8000/backend/api/delete_entrance/${this.entrance_for_delete}/`, {
          headers: {
            "Content-Type": "application/json",
          },
        });

        await this.store.getEntrances();

      } catch (error) {
        console.error("Error deleting entrance:", error);
        alert("Failed to delete entrance.");
      }
    },

  },
};
</script>

<template>

  <div class="manage-entrances">

    <h1>Manage Entrance</h1>

    <div class="create-entrance-page">
      <h2>Create Entrance</h2>
      <form @submit.prevent="submitEntranceForm" class="entrance-form">
        <!-- Building Dropdown -->
        <div class="form-group">
          <label for="building">Entrance Building:</label><br>
          <select v-model="this.entrance_building" id="entrance_building" required>
            <option value="" disabled>Select a Building</option>
            <option v-for="building in this.store.buildings" :key="building.id" :value="building.id">
              {{ building.address }} - {{ building.number }}
            </option>
          </select>
        </div>

        <!-- Entrance Number Field -->
        <div class="form-group">
          <label for="number">Entrance Number:</label><br>
          <input v-model="this.entrance_number" type="text" id="entrance_number" required />
        </div>

        <!-- Submit Button -->
        <button type="submit" class="btn btn-primary">Add Entrance</button>
      </form>
    </div>

    <div>
      <h2>Delete an Entrance</h2>
      <form @submit.prevent="deleteEntranceForm" class="delete-entrance-form">

        <div class="form-group">
          <label for="entranceSelect">Select Entrance to Delete:</label><br>
          <select v-model="this.entrance_for_delete" id="entrance_for_delete" required>
            <option value="" disabled>Select an Entrance</option>
            <option v-for="entrance in this.store.entrances" :key="entrance.id" :value="entrance.id">
              {{ entrance.building }} - {{ entrance.number }}
            </option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">Delete Entrance</button>
      </form>
    </div>
  </div>

</template>