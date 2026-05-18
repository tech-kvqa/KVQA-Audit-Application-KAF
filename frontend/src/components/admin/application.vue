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
        <v-toolbar-title>Dashboard</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn color="error" @click="logout">Logout</v-btn>
      </v-app-bar> -->
  
      <!-- Main Content -->
      <v-main>
        <v-container>
            <h2>Application Page</h2>
            <!-- Tabs for Sales & Consultant Applications -->
            <v-tabs v-model="tab">
              <v-tab value="sales">Applications from Sales</v-tab>
              <v-tab value="consultants">Applications from Consultants</v-tab>
            </v-tabs>

            <v-window v-model="tab">
              <!-- Sales Applications Tab -->
              <v-window-item value="sales">
                <v-data-table
                  :headers="headers_sales"
                  :items="salesApplications"
                  class="elevation-1"
                >
                  <!-- <template v-slot:item.index="{ index }">
                    {{ index + 1 }}
                  </template> -->
                  <!-- Status Column (Only Button for Submitted) -->
                  <template #[`item.status`]="{ item }">
                    <v-btn 
                      v-if="item.status === 'Submitted'" 
                      color="primary" 
                      @click="goToSendQuotation(item.id)">
                      Send Quotation
                    </v-btn>

                    <v-chip v-else :color="item.status === 'Pending' ? 'orange' : 'green'">
                      {{ item.status }}
                    </v-chip>
                  </template>

                  <!-- Delete button -->
                  <template #[`item.actions`]="{ item }">
                      <v-btn color="red" text @click="deleteCompany(item.id)">Delete</v-btn>
                  </template>
                </v-data-table>
              </v-window-item>

              <!-- Consultants Applications Tab -->
              <v-window-item value="consultants">
                <v-data-table
                  :headers="headers"
                  :items="consultantsApplications"
                  class="elevation-1"
                >
                  <template v-slot:item.index="{ index }">
                    {{ index + 1 }}
                  </template>
                </v-data-table>
              </v-window-item>
            </v-window>
        </v-container>
      </v-main>
    </v-app>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      tab: "sales", // Default selected tab
      salesApplications: [],
      consultantsApplications: [],
      // applications: [],

      headers_sales: [
        { title: "ID", key: "id", align: "center", width: "10%" },
        { title: "Company Name", key: "name", align: "center", width: "25%" },
        { title: "Email", key: "email", align: "center", width: "25%" },
        { title: "Director", key: "director", align: "center", width: "25%" },
        { title: "Questionnaire Type", key: "questionnaire_type", align: "center", width: "20%" },
        { title: "Date Sent", key: "date_sent", align: "center", width: "15%" },
        { title: "Status", key: "status", align: "center", width: "15%"},
        // { title: "Submission Link", key: "submission_link", align: "center", width: "15%" },
        { title: "Actions", key: "actions", align: "center", width: "10%" }
      ],
      headers: [
        { title: "ID", key: "id", align: "center", width: "10%" },
        { title: "Company Name", key: "name", align: "center", width: "25%" },
        { title: "Address", key: "address", align: "center", width: "25%" }, // Address added
        { title: "Director", key: "director", align: "center", width: "20%" },
      ]
    };
  },

  mounted() {
    this.fetchApplications();
  },
    methods: {
        logout() {
            localStorage.removeItem('token');
            this.$router.push('/admin/login');
        },

//         async fetchApplications() {
//   try {
//     const [salesResponse, consultantsResponse] = await Promise.all([
//       axios.get("https://kvqa-aduit-application.onrender.com/sales/get-companies"),
//       axios.get("https://kvqa-aduit-application.onrender.com/company_data"),
//     ]);

//     // Ensure sales data is an array
//     const salesData = Array.isArray(salesResponse.data)
//       ? salesResponse.data.map((item) => ({
//           name: item.name,
//           address: item.address, // No address field in sales data, replace with placeholder
//           director: item.director,
//           source: "Sales",
//         }))
//       : [];

//     // Extract consultants data from "comp_data" key
//     const consultantsData =
//       Array.isArray(consultantsResponse.data.comp_data) // Ensure consultants data is an array
//         ? consultantsResponse.data.comp_data.map((item) => ({
//             name: item.organization,
//             address: item.address,
//             director: item.director,
//             source: "Consultant",
//           }))
//         : [];

//     this.applications = [...salesData, ...consultantsData];
//   } catch (error) {
//     console.error("Error fetching applications:", error);
//   }
// }

    async fetchApplications() {
      try {
        const [salesResponse, consultantsResponse] = await Promise.all([
          axios.get("https://kvqa-aduit-application.onrender.com/sales/get-companies"),
          axios.get("https://kvqa-aduit-application.onrender.com/company_data")
        ]);

        // Process Sales Applications
        this.salesApplications = Array.isArray(salesResponse.data)
          ? salesResponse.data.map((company) => ({
              id: company.id,
              name: company.name,
              email: company.email,
              director: company.director,
              questionnaire_type: company.audit_type,  // ✅ Ensure correct field mapping
              date_sent: company.date_sent,
              status: company.status,
              source: "Sales"
            }))
          : [];

        // Process Consultant Applications
        this.consultantsApplications = Array.isArray(consultantsResponse.data.comp_data)
          ? consultantsResponse.data.comp_data.map((item) => ({
              id: item.id,
              name: item.organization,
              address: item.address,
              director: item.director,
              source: "Consultant"
            }))
          : [];
      } catch (error) {
        console.error("Error fetching applications:", error);
      }
    }
  }
};
</script>