<template>
  <v-app>
    <v-navigation-drawer app>
      <v-list>
        <v-list-item link to="/decision-maker/dashboard">
          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item @click="logout" link>
          <v-list-item-content>
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <v-container>
        <v-card class="pa-5 mx-auto mb-6" max-width="800">
          <v-card-title class="text-center text-h5">
            Welcome to Decision Maker Dashboard
          </v-card-title>
          <v-card-text class="text-center">
            <p>You are logged in as Decision Maker: <b>{{ decisionUsername }}</b></p>
            <p>Only assigned applications with uploaded KAF forms are shown below.</p>
          </v-card-text>
        </v-card>

        <v-card>
          <v-card-title class="text-h6 font-weight-bold">
            Assigned Applications
          </v-card-title>

          <v-card-text>
            <v-data-table
              :headers="headers"
              :items="applications"
              class="elevation-1 mt-4"
              dense
            >
              <template #[`item.view`]="{ item }">
                <v-btn color="green" text @click="goToDetailsPage(item.company_id)">
                  View
                </v-btn>
              </template>

              <template #[`item.download`]="{ item }">
                <v-btn color="blue" text @click="openApplication(item)">
                  Download
                </v-btn>
              </template>

              <template #[`item.approve`]="{ item }">
                <v-btn
                  color="success"
                  text
                  :disabled="item.decision_status !== 'Pending'"
                  @click="makeDecision(item.company_id, 'Approved')"
                >
                  Approve
                </v-btn>
              </template>

              <template #[`item.reject`]="{ item }">
                <v-btn
                  color="error"
                  text
                  :disabled="item.decision_status !== 'Pending'"
                  @click="makeDecision(item.company_id, 'Rejected')"
                >
                  Reject
                </v-btn>
              </template>
            </v-data-table>
          </v-card-text>
        </v-card>

        <v-dialog v-model="viewDialog" max-width="1000">
          <v-card>
            <v-card-title class="text-h6 font-weight-bold">
              {{ selectedCompany?.company_name }} - KAF Forms
            </v-card-title>

            <v-card-text style="max-height: 75vh; overflow-y: auto;">
              <v-data-table
                v-if="selectedCompany"
                :headers="kafHeaders"
                :items="selectedCompany.kafs"
                class="elevation-1"
                dense
              >
                <template #[`item.view`]="{ item }">
                  <v-btn
                    v-if="item.file_exists"
                    color="green"
                    text
                    @click="viewFile(item.kaf_type)"
                  >
                    View
                  </v-btn>
                  <v-btn v-else color="grey" text disabled>
                    Not Uploaded
                  </v-btn>
                </template>

                <template #[`item.download`]="{ item }">
                  <v-btn
                    v-if="item.file_exists"
                    color="blue"
                    text
                    @click="downloadFile(item.kaf_type)"
                  >
                    Download
                  </v-btn>
                  <v-btn v-else color="grey" text disabled>
                    Not Uploaded
                  </v-btn>
                </template>
              </v-data-table>
            </v-card-text>

            <v-card-actions>
              <v-spacer />
              <v-btn @click="viewDialog = false">Close</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      applications: [],
      viewDialog: false,
      selectedCompany: null,
      decisionMakerId: null,
      token: null,
      decisionUsername: "",

      headers: [
        { title: "ID", key: "company_id", align: "center" },
        { title: "Company Name", key: "company_name", align: "center" },
        { title: "Submitted At", key: "submitted_at", align: "center" },
        { title: "Status", key: "decision_status", align: "center" },
        { title: "View", key: "view", align: "center" },
        { title: "Download", key: "download", align: "center" },
        { title: "Approve", key: "approve", align: "center" },
        { title: "Reject", key: "reject", align: "center" }
      ],

      kafHeaders: [
        { title: "KAF Type", key: "kaf_type", align: "center" },
        { title: "File Status", key: "file_status", align: "center" },
        { title: "View", key: "view", align: "center" },
        { title: "Download", key: "download", align: "center" }
      ]
    };
  },

  mounted() {
    this.loadDecisionMaker();
  },

  methods: {
    loadDecisionMaker() {
      this.token = localStorage.getItem("decision_token");
      this.decisionMakerId = localStorage.getItem("decision_maker_id");
      this.decisionUsername = localStorage.getItem("decision_username") || "";

      if (!this.token || !this.decisionMakerId) {
        this.$router.replace("/decision-maker/login");
        return;
      }

      this.fetchApplications();
    },

    async fetchApplications() {
      try {
        const res = await axios.get(
          `https://kvqa-aduit-application.onrender.com/decision-maker/applications/${this.decisionMakerId}`,
          {
            headers: {
              Authorization: `Bearer ${this.token}`
            }
          }
        );

        this.applications = (res.data || []).map(app => ({
          ...app,
          submitted_at: app.submitted_at || "",
          decision_status: app.decision_status || "Pending",
          kafs: (app.kafs || []).map(k => ({
            kaf_type: k.kaf_type,
            file_exists: !!k.file_exists
          }))
        }));
      } catch (error) {
        console.error("Error fetching applications:", error);
      }
    },

    openApplication(item) {
      this.selectedCompany = item;
      this.viewDialog = true;
    },

    viewFile(kafType) {
      if (!this.selectedCompany) return;

      window.open(
        `https://kvqa-aduit-application.onrender.com/view-kaf/${this.selectedCompany.company_id}/${kafType}`,
        "_blank"
      );
    },

    downloadFile(kafType) {
      if (!this.selectedCompany) return;

      window.open(
        `https://kvqa-aduit-application.onrender.com/view-kaf/${this.selectedCompany.company_id}/${kafType}`,
        "_blank"
      );
    },

    async makeDecision(companyId, decision) {
      if (!confirm(`Are you sure you want to ${decision.toLowerCase()} this project?`)) {
        return;
      }

      try {
        await axios.post(
          `https://kvqa-aduit-application.onrender.com/decision-maker/decision/${companyId}`,
          { decision },
          {
            headers: {
              Authorization: `Bearer ${this.token}`
            }
          }
        );

        alert(`Project ${decision.toLowerCase()} successfully.`);
        this.fetchApplications();
      } catch (error) {
        console.error("Decision failed:", error);
        alert("Unable to update decision.");
      }
    },

    logout() {
      localStorage.removeItem("decision_token");
      localStorage.removeItem("decision_maker_id");
      localStorage.removeItem("decision_username");
      this.$router.replace("/decision-maker/login");
    },
    goToDetailsPage(companyId) {
      this.$router.push(`/decision-maker/details/${companyId}`);
    },
  }
};
</script>

<style scoped>
.v-container {
  padding: 20px;
}
</style>