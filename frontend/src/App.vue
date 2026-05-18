<template>
  <v-app>
    <v-main>
      <v-app-bar app color="#9e170a" dark>
        <v-toolbar-title>KVQA Assessment</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn color="white" v-if="isLoggedIn" @click="logout">Logout</v-btn>
        <!-- <v-btn color="white" v-else @click="home">Home</v-btn> -->
        <v-btn v-else-if="!isUploadPage" color="white" @click="home">Home</v-btn>
      </v-app-bar>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data () {
    return {
      isLoggedIn: false
    }
  },

  computed: {
    isUploadPage() {
      return this.$route.path.startsWith('/upload');  // ✅ Hide button on Upload page
    }
  },

  created() {
    this.checkLoginStatus();
  },

  methods: {
    checkLoginStatus() {
      this.isLoggedIn = !!localStorage.getItem("token");
    },

    home() {
      this.$router.push('/');
    },

    logout() {
      const userRole = localStorage.getItem("userRole");
      localStorage.removeItem("token");
      localStorage.removeItem("userRole");
      this.isLoggedIn = false;
      
      if (userRole === "admin") {
        this.$router.push("/admin/login");
      } else if (userRole === "consultant") {
        this.$router.push("/consultant/login");
      } else if (userRole === "sales") {
        this.$router.push("/sales/login");
      } else {
        this.$router.push("/");
      }
    }
  },

  watch: {
    $route() {
      this.checkLoginStatus();
    }
  }
}
</script>
