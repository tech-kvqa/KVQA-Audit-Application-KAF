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


  
          <!-- <v-list-item @click="logout">
            <v-list-item-content>
              <v-list-item-title class="text-red">Logout</v-list-item-title>
            </v-list-item-content>
          </v-list-item> -->
        </v-list>
      </v-navigation-drawer>
  
      <!-- Top App Bar -->
      <!-- <v-app-bar app color="primary" dark>
        <v-toolbar-title>Consultants</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn color="error" @click="logout">Logout</v-btn>
      </v-app-bar> -->
  
      <!-- Main Content -->
      <v-main>
        <v-container>
            <h2>Manage Consultants</h2>
            <v-btn color="primary" @click="dialog = true">Create Consultant</v-btn>

            <!-- Dialog for Creating Consultant -->
            <v-dialog v-model="dialog" max-width="500px">
                <v-card>
                    <v-card-title>
                        <span class="text-h5">Create Consultant</span>
                    </v-card-title>
                    <v-card-text>
                        <v-form ref="form" @submit.prevent="createConsultant">
                            <v-text-field v-model="consultant.username" label="Username" required></v-text-field>
                            <v-text-field v-model="consultant.email" label="Email" type="email" required></v-text-field>
                            <v-text-field v-model="consultant.password" label="Password" type="password" required></v-text-field>
                            <v-btn color="primary" type="submit" block>Create</v-btn>
                        </v-form>
                    </v-card-text>
                </v-card>
            </v-dialog>

            <!-- List of Consultants -->
            <!-- <v-list>
                <v-list-item v-for="consultant in consultants" :key="consultant">
                    <v-list-item-content>
                    <v-list-item-title>{{ consultant }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list> -->
            <!-- List of Consultants -->
            <v-data-table
              :headers="headers"
              :items="consultants"
              class="elevation-1 mt-4"
              dense
            >
              <template #[`item.actions`]="{ item }">
                <v-btn color="red" text @click="deleteConsultant(item.id)">Delete</v-btn>
              </template>
            </v-data-table>
        </v-container>
      </v-main>
    </v-app>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            dialog: false,
            consultant: {
                username: '',
                email: '',
                password: ''
            },
            consultants: [],
            headers: [
                { title: "ID", key: "id", align: "center", width: "10%" },
                { title: "Username", key: "username", align: "center", width: "30%" },
                { title: "Email", key: "email", align: "center", width: "40%" },
                { title: "Actions", key: "actions", align: "center", width: "20%" }
            ]
        };
    },
    methods: {
        async createConsultant() {
            try {
                const response = await axios.post("https://kvqa-audit-application-kaf.onrender.com/consultant", this.consultant);
                alert(response.data.message);
                this.dialog = false;
                this.fetchConsultants();
            } catch (error) {
                alert("Error creating consultant: " + error.response.data.message);
            }
        },

        async fetchConsultants() {
            try {
                const response = await axios.get("https://kvqa-audit-application-kaf.onrender.com/consultant");
                this.consultants = response.data.consultants;
            } catch (error) {
                console.error("Error fetching consultants:", error);
            }
        },

        async deleteConsultant(id) {
            if (confirm("Are you sure you want to delete this consultant?"));
            try{
                const response = await axios.delete(`https://kvqa-audit-application-kaf.onrender.com/consultant/${id}`);
                this.consultants = this.consultants.filter(consultant => consultant.id !== id);
                alert(`Consultant with ID ${id} deleted`);
            } catch (error) {
                alert("Error deleting consultant: " + error.response.data.message);
                alert("Failed to delete consultant.");
            }
        },

        logout() {
            localStorage.removeItem('token');
            this.$router.push('/admin/login');
        },
    },
    mounted() {
        this.fetchConsultants();
    }
};
</script>