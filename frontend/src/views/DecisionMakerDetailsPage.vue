<template>
  <v-app>
    <!-- Sidebar -->
    <v-navigation-drawer app>
      <v-list>
        <v-list-item link to="/decision-maker/dashboard">
          <v-list-item-content>
            <v-list-item-title>Dashboard</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item @click="logout" link>
          <v-list-item-content>
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- Main -->
    <v-main>
      <v-container>

        <!-- Header -->
        <v-card class="mb-4 pa-4">
          <v-card-title class="text-h5">
            {{ companyName }} - KAF Details
          </v-card-title>
        </v-card>

        <!-- KAF Table -->
        <v-card>
          <v-data-table
            :headers="headers"
            :items="kafList"
            class="mt-4"
          >

            <!-- Download -->
            <template #[`item.download`]="{ item }">
              <v-btn
                v-if="item.file_exists"
                color="green"
                @click="downloadFile(item.kaf_type)"
              >
                Download
              </v-btn>

              <v-btn
                v-else
                color="grey"
                disabled
              >
                Not Available
              </v-btn>
            </template>

            <!-- View -->
            <template #[`item.view`]="{ item }">
              <v-btn
                v-if="item.file_exists"
                color="blue"
                @click="viewFile(item.kaf_type)"
              >
                View
              </v-btn>

              <v-btn
                v-else
                color="grey"
                disabled
              >
                Not Available
              </v-btn>
            </template>

          </v-data-table>
        </v-card>

      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      companyId: null,
      companyName: "",

      kafMaster: [
        { code: "KAF1", name: "KAF 01 - Questionnaire" },
        { code: "KAF2", name: "KAF 02 - Contract Review Report" },
        { code: "KAF3", name: "KAF 03 - Certification" },
        { code: "KAF4", name: "KAF 04 - Certification Audit Contract" },
        { code: "KAF5", name: "KAF 05 - Report of Document review audit" },
        { code: "KAF6", name: "KAF 06 - Document review table" },
        { code: "KAF7", name: "KAF 07 - Result of document review (Stage-1)" },
        { code: "KAF8", name: "KAF 08 - On site Audit report" },
        { code: "KAF9", name: "KAF 09 - Audit summary" },
        { code: "KAF10", name: "KAF 10 - Attendance sheet" },
        { code: "KAF12", name: "KAF 12 - Stage 2 Audit Schedule" },
        { code: "KAF13", name: "KAF 13 - Stage 1 Audit Schedule" },
        { code: "KAF14", name: "KAF 14 - Confirmation of certification scope" },
        { code: "KAF15", name: "KAF 15 - No Conflict-of-interest agreement" },
        { code: "KAF17", name: "KAF 17 - Surveillance program" },
        { code: "KAF18", name: "KAF 18 - CAR register" },
        { code: "KAF19", name: "KAF 19 - Corrective action request (CAR)" },
        { code: "KAF20", name: "KAF 20 - Observation reports" },
        { code: "KAF24", name: "KAF 24 - Audit Completion & Certification Record" }
      ],

      kafList: [],

      headers: [
        { title: "KAF", key: "kaf_name" },
        { title: "Date", key: "date" },
        { title: "View", key: "view" },
        { title: "Download", key: "download" }
      ]
    };
  },

  mounted() {
    this.companyId = this.$route.params.companyId;

    if (this.companyId) {
      this.fetchCompanyName();
      this.fetchKAF();
    }
  },

  methods: {
    async fetchCompanyName() {
      try {
        const res = await axios.get(
          "https://kvqa-aduit-application.onrender.com/sales/get-companies"
        );

        const company = res.data.find(c => c.id == this.companyId);

        if (company) {
          this.companyName = company.name;
        }

      } catch (err) {
        console.error("Error fetching company name:", err);
      }
    },

    async fetchKAF() {
      try {
        const res = await axios.get(
          `https://kvqa-aduit-application.onrender.com/kaf-status/${this.companyId}`
        );

        const backendData = res.data;

        this.kafList = this.kafMaster.map(kaf => {
          const record = backendData.find(
            r => r.kaf_type === kaf.code
          );

          return {
            kaf_type: kaf.code,
            kaf_name: kaf.name,
            date: record ? record.date : "",
            file_exists: record ? record.file_exists : false
          };
        });

      } catch (error) {
        console.error("Error fetching KAF:", error);
      }
    },

    viewFile(kaf) {
      window.open(
        `https://kvqa-aduit-application.onrender.com/view-kaf/${this.companyId}/${kaf}`,
        "_blank"
      );
    },

    async downloadFile(kaf) {
      try {
        const response = await axios.get(
          `https://kvqa-aduit-application.onrender.com/view-kaf/${this.companyId}/${kaf}`,
          { responseType: "blob" }
        );

        const blob = new Blob([response.data]);
        const url = window.URL.createObjectURL(blob);

        const link = document.createElement("a");
        link.href = url;
        link.download = `${this.companyName}_${kaf}.docx`;

        document.body.appendChild(link);
        link.click();
        link.remove();

      } catch (error) {
        console.error("Download failed:", error);
      }
    },

    logout() {
      localStorage.removeItem("decision_token");
      localStorage.removeItem("decision_maker_id");
      localStorage.removeItem("decision_username");

      this.$router.push("/decision-maker/login");
    }
  }
};
</script>

<style scoped>
.v-container {
  padding: 20px;
}
</style>