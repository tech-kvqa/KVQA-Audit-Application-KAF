<template>
    <v-app>
      <!-- Sidebar Navigation Drawer -->
      <v-navigation-drawer app>
        <v-list>
          <v-list-item link to="/sales/dashboard">
            <v-list-item-content>
              <v-list-item-title>Home</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
  
          <v-list-item link to="/sales/application">
            <v-list-item-content>
              <v-list-item-title>Application</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
  
      <!-- Main Content -->
      <v-main>
        <v-container>
            <v-card class="pa-5 mx-auto" max-width="500">
            <v-card-title class="text-center">Welcome to Dashboard</v-card-title>
            <v-card-text>
              <p>You are logged in!</p>
            </v-card-text>
          </v-card>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
  export default {
    methods: {
      logout() {
        localStorage.removeItem("token");
        this.$router.push("/consultant/login");
      }
    }
  };
  </script>
  
  <style scoped>
  .v-container {
    padding: 20px;
  }
  .text-red {
    color: red;
  }
  </style>