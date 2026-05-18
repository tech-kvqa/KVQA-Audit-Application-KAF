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
          <v-btn color="primary" class="mb-4" @click="navigateToApplicationForm">
            Create new application
          </v-btn>
        </v-container>
      </v-main>
    </v-app>
</template>

<script>
import axios from 'axios';
export default {
    methods: {
        navigateToApplicationForm() {
            this.$router.push('/consultant/applicationform');
        },

        logout() {
            localStorage.removeItem('token');
            this.$router.push('/consultant/login');
        }
    }
};
</script>