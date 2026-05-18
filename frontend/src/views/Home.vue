<template>
    <v-app>
      <v-container class="d-flex flex-column justify-center align-center fill-height">
        <h1 class="text-h3 font-weight-bold mb-6">Welcome to KVQA Audit Application</h1>
        
        <v-card class="pa-6 text-center" width="400">
          <v-card-title class="text-h5">Login as</v-card-title>
          <v-divider class="my-4"></v-divider>
          
          <v-btn color="primary" block class="mb-3" @click="goToLogin('admin')">
            Admin Login
          </v-btn>
          
          <!-- <v-btn color="secondary" block class="mb-3" @click="goToLogin('consultant')">
            Consultant Login
          </v-btn> -->

          <v-btn color="secondary" block class="mb-3" @click="goToLogin('sales')">
            Auditor Login
          </v-btn>

          <v-btn color="secondary" block class="mb-3" @click="goToLogin('decision-maker')">
            Decision Maker Login
          </v-btn>
        </v-card>
      </v-container>
    </v-app>
  </template>
  
  <script>
  import { useRouter } from 'vue-router';
  
  export default {
    setup() {
      const router = useRouter();
  
      const goToLogin = (role) => {
        router.push(`/${role}/login`);
      };
  
      return { goToLogin };
    },
  };
  </script>
  
  <style scoped>
  .v-container {
    background: linear-gradient(to right, #1976D2, #42A5F5);
    height: 100vh;
    color: white;
  }
  </style>
  