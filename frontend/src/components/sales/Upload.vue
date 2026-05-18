<!-- <template>
    <v-container>
      <v-card class="mx-auto mt-10 pa-5" max-width="600">
        <v-card-title>Submit Your Filled Questionnaire</v-card-title>
        <v-card-subtitle>Please upload your filled questionnaire document below.</v-card-subtitle>
  
        <v-card-text>
          <v-file-input 
            label="Upload Filled Form" 
            accept=".pdf,.doc,.docx, .xlsx"
            v-model="file"
            show-size
            outlined
          ></v-file-input>
  
          <v-btn :disabled="!file" color="primary" class="mt-3" @click="submitForm">
            Submit
          </v-btn>
        </v-card-text>
  
        <v-alert v-if="message" :type="messageType" class="mt-4">{{ message }}</v-alert>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        file: null,
        token: this.$route.params.token,  // Extract the token from the URL
        message: '',
        messageType: ''
      };
    },
  
    methods: {
      async submitForm() {
        if (!this.file) {
          this.message = "Please select a file before submitting.";
          this.messageType = "error";
          return;
        }
  
        let formData = new FormData();
        formData.append("file", this.file);
        formData.append("token", this.token);
  
        try {
          const response = await axios.post("https://kvqa-aduit-application.onrender.com/sales/upload", formData, {
            headers: { "Content-Type": "multipart/form-data" }
          });
  
          this.message = response.data.message;
          this.messageType = "success";
  
        } catch (error) {
          this.message = "Failed to upload the form. Please try again.";
          this.messageType = "error";
          console.error(error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .v-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  </style>
   -->



   <template>
    <v-container>
      <v-card class="mx-auto mt-10 pa-5" max-width="600">
        <v-card-title>Submit Your Filled Questionnaire</v-card-title>
        <v-card-subtitle>Please upload your filled questionnaire document below.</v-card-subtitle>
  
        <v-card-text>
          <v-file-input 
            label="Upload Filled Form" 
            accept=".pdf,.doc,.docx,.xlsx"
            v-model="file"
            show-size
            outlined
          ></v-file-input>
  
          <v-btn :disabled="!file" color="primary" class="mt-3" @click="submitForm">
            Submit
          </v-btn>
        </v-card-text>
  
        <v-alert v-if="message" :type="messageType" class="mt-4">{{ message }}</v-alert>

        <!-- <v-btn v-if="message" color="error" class="mt-3" @click="closeWindow">
          Close Window
        </v-btn> -->
      </v-card>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        file: null,
        token: this.$route.params.token,  // Extract the token from the URL
        message: '',
        messageType: ''
      };
    },
  
    methods: {
      async submitForm() {
        if (!this.file) {
          this.message = "Please select a file before submitting.";
          this.messageType = "error";
          return;
        }
  
        let formData = new FormData();
        formData.append("file", this.file);
        formData.append("token", this.token);
  
        try {
          const response = await axios.post("https://kvqa-aduit-application.onrender.com/sales/upload", formData, {
            headers: { "Content-Type": "multipart/form-data" }
          });
  
          this.message = response.data.message;
          this.messageType = "success";
  
          // ✅ Automatically close window after a short delay
          setTimeout(() => {
            window.close();
          }, 2000); // Closes window after 2 seconds
  
        } catch (error) {
          this.message = "Failed to upload the form. Please try again.";
          this.messageType = "error";
          console.error(error);
        }
      },

      // closeWindow() {
      //   window.location.href = "https://kvqa-aduit-application.onrender.com/close-tab";
      // }
    }
  };
  </script>
  
  <style scoped>
  .v-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  </style>
  