<script>
import { RouterView } from "vue-router";
import router from "../router";
import { useStore } from "../stores/store.js";

export default {
  data() {
    return {
      store: useStore(),
    };
  },

  async mounted() {
    if (!this.store.isAuthenticatedState) {
      router.push("/login");
      return;
    }
  },

  methods: {
    // Method to check if the user has access based on their role
    hasAccess(allowedRoles) {
      return allowedRoles.includes(this.store.userRole);
    },

    // Navigation function (replace with actual navigation code)
    navigate(routeName) {
      this.$router.push({ name: routeName });
    },

    logout() {
      this.$router.push("/login");
    },
  },
};
</script>

<template>
  <nav class="navbar">
    <ul class="navbar-nav">
      <li>
        <button @click="this.$router.push('/')">Main</button>
      </li>
      <!-- Inhabitants button (Visible to all roles except Inhabitants) -->
      <li v-if="hasAccess(['admin', 'manager', 'guard'])">
        <button @click="this.$router.push('/inhabitant')">Inhabitant</button>
      </li>

      <!-- Guards button (Visible to Admin and Manager) -->
      <li v-if="hasAccess(['admin', 'manager'])">
        <button @click="this.$router.push('/guard')">Guard</button>
      </li>

      <!-- Managers button (Visible only to Admin) -->
      <li v-if="hasAccess(['admin'])">
        <button @click="this.$router.push('/manager')">Manager</button>
      </li>

      <!-- Buildings button (Visible only to Admin) -->
      <li v-if="hasAccess(['admin'])">
        <button @click="this.$router.push('/building')">Building</button>
      </li>

      <!-- Entrances button (Visible to Admin and Manager) -->
      <li v-if="hasAccess(['admin', 'manager'])">
        <button @click="this.$router.push('/entrance')">Entrance</button>
      </li>

      <!-- Apartments button (Visible to Admin, Manager and Guard) -->
      <li v-if="hasAccess(['admin', 'manager', 'guard'])">
        <button @click="this.$router.push('/apartment')">Apartment</button>
      </li>

      <!-- Logout button (Visible to all roles) -->
      <li>
        <button @click="logout">Logout</button>
      </li>
    </ul>
  </nav>
  <br />
  <div v-if="this.store.isAuthenticatedState">
    <RouterView />
  </div>
</template>

<style scoped>
.navbar {
  background-color: #333;
  padding: 10px;
  position: fixed; /* Keeps it fixed at the top */
  top: 0; /* Aligns it to the top of the page */
  left: 0;
  width: 100%; /* Full width of the viewport */
  z-index: 1000; /* Ensures it stays on top of other elements */
}

.navbar-nav {
  display: flex;
  flex-direction: row;
  list-style: none;
  padding: 0;
  margin: 0;
  align-items: center;
}

.navbar-nav li {
  margin-right: 15px;
}

.navbar-nav button {
  color: white;
  background: transparent;
  border: none;
  padding: 10px 15px;
  cursor: pointer;
  font-size: 1rem;
}

.navbar-nav button:hover {
  background-color: #555;
  border-radius: 5px;
}
</style>
