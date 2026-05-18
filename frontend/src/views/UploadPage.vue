<template>
  <v-container>
    <v-card>
      <v-card-title>Upload Documents</v-card-title>

      <v-form>
        <div v-for="kaf in kafTypes" :key="kaf">
          <v-file-input
            :label="kaf"
            @change="file => handleFile(file, kaf)"
          />
        </div>

        <v-btn color="primary" @click="uploadFiles">
          Upload
        </v-btn>
      </v-form>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      companyId: this.$route.params.id,
      files: {},
      kafTypes: ["KAF1", "KAF2", "KAF3", "KAF4"]
    };
  },

  methods: {
    handleFile(file, type) {
      this.files[type] = file;
    },

    async uploadFiles() {
      const formData = new FormData();

      Object.keys(this.files).forEach(type => {
        formData.append(type, this.files[type]);
      });

      try {
        await axios.post(
          `https://kvqa-audit-application-kaf.onrender.com/upload/${this.companyId}`,
          formData
        );

        alert("Files uploaded successfully");
      } catch (err) {
        console.error(err);
      }
    }
  }
};
</script>