<!-- <template>
    <v-container fluid>
      <v-app-bar app color="primary" dark>
        <v-app-bar-title>Admin Dashboard</v-app-bar-title>
        <v-spacer></v-spacer>
        <v-btn @click="logout" color="error">Logout</v-btn>
      </v-app-bar>
  
      <v-main>
        <v-container>
          <h2>Welcome, Admin!</h2>
          <p>This is your dashboard. Manage users, view reports, and configure settings.</p>
          
          <v-row>
            <v-col cols="12" sm="6" md="4">
              <v-card class="pa-4" outlined>
                <v-card-title>Manage Users</v-card-title>
                <v-card-text>View and manage user accounts.</v-card-text>
                <v-card-actions>
                  <v-btn color="primary">Go to Users</v-btn>
                </v-card-actions>
              </v-card>
            </v-col>
  
            <v-col cols="12" sm="6" md="4">
              <v-card class="pa-4" outlined>
                <v-card-title>Reports</v-card-title>
                <v-card-text>View system and activity reports.</v-card-text>
                <v-card-actions>
                  <v-btn color="primary">View Reports</v-btn>
                </v-card-actions>
              </v-card>
            </v-col>
  
            <v-col cols="12" sm="6" md="4">
              <v-card class="pa-4" outlined>
                <v-card-title>Settings</v-card-title>
                <v-card-text>Configure application settings.</v-card-text>
                <v-card-actions>
                  <v-btn color="primary">Open Settings</v-btn>
                </v-card-actions>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
    </v-container>
  </template>
  
  <script>
  export default {
    created() {
      const token = localStorage.getItem('token');
      if (!token) {
        this.$router.push('/'); // Redirect to login if not authenticated
      }
    },
    methods: {
      logout() {
        localStorage.removeItem('token'); // Clear token
        this.$router.push('/admin/login'); // Redirect to login page
      }
    }
  };
  </script>
  
  <style scoped>
  .v-container {
    background: #f5f5f5;
    min-height: 100vh;
  }
  </style>
   -->


  <template>
    <v-app>
      <!-- Sidebar Navigation Drawer -->
      <v-navigation-drawer app>
        <v-list>
          <v-list-item link to="/admin/dashboard">
            <v-list-item-content>
              <v-list-item-title>Home</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
  
          <v-list-item link to="/admin/application">
            <v-list-item-content>
              <v-list-item-title>Application</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
  
          <v-list-item link to="/admin/users">
            <v-list-item-content>
              <v-list-item-title>Manage Users</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item link to="/admin/consultants">
            <v-list-item-content>
              <v-list-item-title>Manage Consultants</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item link to="/admin/sales">
            <v-list-item-content>
              <v-list-item-title>Manage Sales</v-list-item-title>
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
        this.$router.push("/admin/login");
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
  
  