<template>
    <v-app>
      <!-- Sidebar Navigation Drawer -->
      <v-navigation-drawer app>
        <v-list>
          <v-list-item link to="/consultant/dashboard">
            <v-list-item-content>
              <v-list-item-title>Home</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
  
          <v-list-item link to="/consultant/application">
            <v-list-item-content>
              <v-list-item-title>Application</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
  
          <!-- <v-list-item link to="/admin/users">
            <v-list-item-content>
              <v-list-item-title>Manage Users</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item link to="/admin/consultants">
            <v-list-item-content>
              <v-list-item-title>Manage Consultants</v-list-item-title>
            </v-list-item-content>
          </v-list-item> -->

          <!-- <v-list-item @click="logout">
            <v-list-item-content>
              <v-list-item-title class="text-red">Logout</v-list-item-title>
            </v-list-item-content>
          </v-list-item> -->
        </v-list>
      </v-navigation-drawer>
  
      <!-- Top App Bar -->
      <!-- <v-app-bar app color="primary" dark>
        <v-toolbar-title>Dashboard</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn color="error" @click="logout">Logout</v-btn>
      </v-app-bar> -->
  
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