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
          <h2>Questionnaire Page</h2>
          <!-- Small Dropdown for Certification Selection -->
        <v-select
          v-model="selectedCertification"
          :items="certifications"
          label="Select Certification"
          density="compact"
          outlined
          class="mb-4"
          style="max-width: 250px;" 
        ></v-select>
        </v-container>
      </v-main>
    </v-app>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            selectedCertification: null,
            certifications: ['QMS', 'EMS', 'ISMS', 'FSMS', 'OHSAS']
        };
    },
    methods: {
        navigateToApplicationForm() {
            this.$router.push('/consultant/applicationform');
        },

        logout() {
            localStorage.removeItem('token');
            this.$router.push('/consultant/login');
        }
    },

    watch: {
      selectedCertification(newVal) {
        if (newVal) {
          this.$router.push(`/consultant/questionnaire/${newVal.toLowerCase()}`);
        }
      },
    },
};
</script>