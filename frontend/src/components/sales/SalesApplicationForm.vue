<template>
  <v-container>
    <v-card class="pa-5">
      <v-card-title>Send Certification Questionnaire</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="sendEmail">
          <v-text-field v-model="company.name" label="Company Name" required></v-text-field>
          <v-text-field v-model="company.address" label="Address" required></v-text-field>
          <v-text-field v-model="company.director" label="Director Name" required></v-text-field>
          <v-text-field v-model="company.email" label="Company Email" required></v-text-field>

          <v-select v-model="selectedQuestionnaire" :items="questionnaireTypes"
                    label="Select Certification Form" required></v-select>

          <v-btn type="submit" color="primary">Send Questionnaire</v-btn>
        </v-form>

        <v-alert v-if="message" type="success" class="mt-4">{{ message }}</v-alert>
      </v-card-text>
    </v-card>
  </v-container>
</template>
  
<script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        company: {
          name: "",
          address: "",
          director: "",
          email: ""
        },
        selectedQuestionnaire: null,
        questionnaireTypes: [],
        message: ""
      };
    },
    mounted() {
      this.fetchQuestionnaireTypes();
    },
    methods: {
      async fetchQuestionnaireTypes() {
        try {
          const response = await axios.get("https://kvqa-aduit-application.onrender.com/sales/get-questionnaire-types");
          this.questionnaireTypes = response.data;
        } catch (error) {
          console.error("Error fetching questionnaire types:", error);
        }
      },
      async sendEmail() {
        if (!this.selectedQuestionnaire) {
          alert("Please select a certification form.");
          return;
        }
  
        try {
          const response = await axios.post("https://kvqa-aduit-application.onrender.com/sales/send-email", {
            company_name: this.company.name,
            address: this.company.address,
            director: this.company.director,
            email: this.company.email,
            questionnaire_type: this.selectedQuestionnaire
          });
  
          this.message = response.data.message;
          this.company = { name: "", address: "", director: "", email: "" };
          this.selectedQuestionnaire = null;
          this.$router.push("/sales/application");
        } catch (error) {
          console.error("Error sending email:", error);
        }
      }
    }
  };
</script>
  