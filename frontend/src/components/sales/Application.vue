<template>
    <v-app>
      <!-- Sidebar Navigation Drawer -->
      <v-navigation-drawer app>
        <v-list>
          <v-list-item link to="/sales/dashboard">
            <v-list-item-content>
              <v-list-item-title>Home</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
  
          <v-list-item link to="/sales/application">
            <v-list-item-content>
              <v-list-item-title>Application</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
  
      <!-- Main Content -->
      <v-main>
        <v-container>
          <v-btn color="primary" class="mb-4" @click="navigateToApplicationForm">
            Create new application
          </v-btn>

          <v-card-text>
            <v-data-table :headers="headers" :items="companies" class="elevation-1 mt-4" dense>

              <!-- Status Column -->
              <!-- <template #[`item.status`]="{ item }">
                <v-chip :color="item.status === 'Pending' ? 'orange' : 'green'">
                  {{ item.status === 'Pending' ? 'Pending' : 'Send Quotation' }}
                </v-chip>
              </template> -->

              <!-- Status Column (Only Button for Submitted) -->
              <!-- <template #[`item.status`]="{ item }">
                <v-btn 
                  v-if="item.status === 'Submitted'" 
                  color="primary" 
                  @click="goToSendQuotation(item.id)">
                  Send Quotation
                </v-btn> -->

                

                <!-- <v-chip v-else :color="item.status === 'Pending' ? 'orange' : 'green'">
                  {{ item.status }}
                </v-chip>
              </template> -->

              <template #[`item.details`]="{ item }">
                <v-btn color="green" text @click="goToDetailsPage(item.id)">
                  View Details
                </v-btn>
              </template>

              <!-- Submission Link Column -->
              <!-- <template #[`item.submission_link`]="{ item }">
                <v-btn color="blue" text @click="copySubmissionLink(item.submission_link)">
                  Copy Link
                </v-btn>
              </template> -->

              <!-- Delete button -->
              <template #[`item.actions`]="{ item }">
                  <v-btn color="red" text @click="deleteCompany(item.id)">Delete</v-btn>
              </template>

              <!-- View Column -->
              <template #[`item.view`]="{ item }">
                <v-btn color="blue" text 
                      @click="viewExcelFile(item.name, item.questionnaire_type)">
                  View
                </v-btn>
              </template>
            </v-data-table>
          </v-card-text>
        </v-container>
      </v-main>
    </v-app>
</template>

<script>
import axios from 'axios';
export default {
  data () {
    return {
      companies: [],  // Stores fetched company data
      headers: [
        { title: "ID", key: "id", align: "center", width: "10%" },
        { title: "Company Name", key: "name", align: "center", width: "25%" },
        // { title: "Email", key: "email", align: "center", width: "25%" },
        // { title: "Director", key: "director", align: "center", width: "25%" },
        { title: "Questionnaire Type", key: "questionnaire_type", align: "center", width: "20%" },
        { title: "Date Sent", key: "date_sent", align: "center", width: "15%" },
        // { title: "Status", key: "status", align: "center", width: "15%"},
        { title: "Details", key: "details", align: "center", width: "15%" },
        // { title: "Submission Link", key: "submission_link", align: "center", width: "15%" },
        { title: "Actions", key: "actions", align: "center", width: "10%" },
        // { title: "View", key: "view", align: "center", width: "10%" }
      ]
    }
  },

  mounted() {
    this.fetchCompanyData();
  },

  methods: {
    navigateToApplicationForm() {
        this.$router.push('/sales/applicationform');
    },

    async fetchCompanyData() {
      try {
        const response = await axios.get("https://kvqa-aduit-application.onrender.com/sales/get-companies");
        this.companies = response.data.map(company => ({
            id: company.id,
            name: company.name,
            email: company.email,
            director: company.director,
            questionnaire_type: company.audit_type,  // ✅ Ensure correct field mapping
            date_sent: company.date_sent,
            status: company.status,
            submission_link: `http://127.0.0.1:8080/upload/${company.token}`
        }));
      } catch (error) {
        console.error ("Error fetching company data:", error);
      }
    },

    async deleteCompany(id) {
        if (!confirm("Are you sure you want to delete this company?")) return;
        try {
            await axios.delete(`https://kvqa-aduit-application.onrender.com/sales/delete-company/${id}`);
            this.fetchCompanyData(); // Refresh list after deletion
        } catch (error) {
            console.error("Error deleting company:", error);
        }
    },

    copySubmissionLink(link) {
      navigator.clipboard.writeText(link).then(() => {
        alert("Submission link copied!");
      }).catch(err => {
        console.error("Failed to copy link:", err);
      });
    },

    logout() {
        localStorage.removeItem('token');
        this.$router.push('/consultant/login');
    },

    goToSendQuotation(companyId) {
      this.$router.push(`/sales/send-quotation/${companyId}`);
    },

    viewExcelFile(companyName, questionnaireType) {
      this.$router.push(`/sales/view-excel/${companyName}/${questionnaireType}`);
    },

    goToDetailsPage(companyId) {
      this.$router.push(`/sales/details/${companyId}`);
    }
  }
};
</script>