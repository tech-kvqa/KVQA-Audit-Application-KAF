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
        <v-toolbar-title>Consultants</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn color="error" @click="logout">Logout</v-btn>
      </v-app-bar> -->
  
      <!-- Main Content -->
      <v-main>
        <v-container>
            <h2>Manage Sales</h2>
            <v-btn color="primary" @click="dialog = true">Create Sales Executive</v-btn>

            <!-- Dialog for Creating Consultant -->
            <v-dialog v-model="dialog" max-width="500px">
                <v-card>
                    <v-card-title>
                        <span class="text-h5">Create Sales</span>
                    </v-card-title>
                    <v-card-text>
                        <v-form ref="form" @submit.prevent="createsalesexecutive">
                            <v-text-field v-model="sales.username" label="Username" required></v-text-field>
                            <v-text-field v-model="sales.email" label="Email" type="email" required></v-text-field>
                            <v-text-field v-model="sales.password" label="Password" type="password" required></v-text-field>
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
            <!-- List of Sale Executives -->
            <v-data-table
              :headers="headers"
              :items="salesexecutive"
              class="elevation-1 mt-4"
              dense
            >
              <template #[`item.actions`]="{ item }">
                <v-btn color="red" text @click="deleteSalesExecutives(item.id)">Delete</v-btn>
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
            sales: {
                username: '',
                email: '',
                password: ''
            },
            salesexecutive: [],
            headers: [
                { title: "ID", key: "id", align: "center", width: "10%" },
                { title: "Username", key: "username", align: "center", width: "30%" },
                { title: "Email", key: "email", align: "center", width: "40%" },
                { title: "Actions", key: "actions", align: "center", width: "20%" }
            ]
        };
    },
    methods: {
        async createsalesexecutive() {
            try {
                const response = await axios.post("https://kvqa-aduit-application.onrender.com/sales", this.sales);
                alert(response.data.message);
                this.dialog = false;
                this.fetchSalesExecutives();
            } catch (error) {
                alert("Error creating consultant: " + error.response.data.message);
            }
        },

        async fetchSalesExecutives() {
            try {
                const response = await axios.get("https://kvqa-aduit-application.onrender.com/sales");
                console.log(response)
                this.salesexecutive = response.data.Sales;
            } catch (error) {
                console.error("Error fetching consultants:", error);
            }
        },

        async deleteSalesExecutives(id) {
            if (confirm("Are you sure you want to delete this consultant?"));
            try{
                const response = await axios.delete(`https://kvqa-aduit-application.onrender.com/sales/${id}`);
                this.salesexecutive = this.salesexecutive.filter(sales => sales.id !== id);
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
        this.fetchSalesExecutives();
    }
};
</script>