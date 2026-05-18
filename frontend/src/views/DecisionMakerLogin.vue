<template>
  <v-container class="d-flex justify-center align-center" style="min-height: 80vh;">
    <v-card width="420" class="pa-6">
      <v-card-title class="text-h5 font-weight-bold">
        Decision Maker Login
      </v-card-title>

      <v-card-text>
        <v-text-field
          v-model="username"
          label="Username"
          prepend-inner-icon="mdi-account"
        />

        <v-text-field
          v-model="password"
          label="Password"
          type="password"
          prepend-inner-icon="mdi-lock"
        />

        <v-alert v-if="error" type="error" class="mt-3">
          {{ error }}
        </v-alert>
      </v-card-text>

      <v-card-actions>
        <v-btn color="primary" block :loading="loading" @click="login">
          Login
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      loading: false,
      error: ""
    };
  },
  methods: {
    async login() {
      this.error = "";
      this.loading = true;

      try {
        const res = await axios.post("https://kvqa-aduit-application.onrender.com/decision-maker/login", {
          username: this.username,
          password: this.password
        });

        localStorage.setItem("decision_token", res.data.access_token);
        localStorage.setItem("decision_maker_id", res.data.decision_maker_id);
        localStorage.setItem("decision_username", res.data.username);

        this.$router.replace("/decision-maker/dashboard");
      } catch (err) {
        this.error = err.response?.data?.message || "Login failed";
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>