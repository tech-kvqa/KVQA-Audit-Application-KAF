<template>
    <v-container class="d-flex justify-center align-center fill-height">
      <v-card width="400" class="pa-6">
        <v-card-title class="text-h5 text-center">Consultant Login</v-card-title>
        <v-divider class="my-4"></v-divider>
  
        <v-form @submit.prevent="login">
          <v-text-field v-model="username" label="Username" prepend-icon="mdi-account" required></v-text-field>
  
          <v-text-field 
            v-model="password" 
            label="Password" 
            prepend-icon="mdi-lock" 
            :type="showPassword ? 'text' : 'password'" 
            required
          >
            <template v-slot:append>
              <v-icon @click="showPassword = !showPassword">
                {{ showPassword ? 'mdi-eye-off' : 'mdi-eye' }}
              </v-icon>
            </template>
          </v-text-field>
  
          <v-btn color="secondary" block type="submit">Login</v-btn>
        </v-form>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        username: '',
        password: '',
        showPassword: false
      };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post("https://kvqa-aduit-application.onrender.com/consultant/login", {
            username: this.username,
            password: this.password
          });
          localStorage.setItem('token', response.data.token);
          localStorage.setItem('userRole', 'consultant');
          this.$router.push('/consultant/dashboard');
        } catch (error) {
          console.error(error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .v-container {
    background: linear-gradient(to right, #004D40, #00796B);
    height: 100vh;
    color: white;
  }
  </style>
  