<!-- <template>
  <v-container>
    <v-card>
      <v-card-title>KAF Details</v-card-title>

      <v-data-table :headers="headers" :items="kafList" class="mt-4">

        <template #[`item.action`]="{ item }">

          <v-btn 
            v-if="item.file_exists" 
            color="green" 
            @click="viewFile(item.kaf_type)">
            View
          </v-btn>

          <v-btn 
            v-else 
            color="orange" 
            @click="openUpload(item.kaf_type)">
            Upload
          </v-btn>

        </template>

      </v-data-table>
    </v-card>

    <v-dialog v-model="dialog" width="400">
      <v-card>
        <v-card-title>Upload {{ selectedKaf }}</v-card-title>

        <v-card-text>
          <v-file-input v-model="file" label="Select File" />
        </v-card-text>

        <v-card-actions>
          <v-btn color="primary" @click="uploadFile">Upload</v-btn>
          <v-btn text @click="dialog = false">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      companyId: null,   // ✅ FIXED
      kafList: [],
      headers: [
        { title: "KAF", key: "kaf_type" },
        { title: "Date", key: "date" },
        { title: "Action", key: "action" }
      ],
      dialog: false,
      selectedKaf: null,
      file: null
    };
  },

  mounted() {
    // ✅ FIX: get param properly
    this.companyId = this.$route.params.companyId;

    console.log("Company ID:", this.companyId); // debug

    if (this.companyId) {
      this.fetchKAF();
    } else {
      console.error("Company ID is undefined!");
    }
  },

  methods: {
    async fetchKAF() {
      try {
        const res = await axios.get(
          `https://kvqa-aduit-application.onrender.com/kaf-status/${this.companyId}`
        );
        this.kafList = res.data;
      } catch (error) {
        console.error("Error fetching KAF:", error);
      }
    },

    // viewFile(kaf) {
    // //   window.open(
    // //     `https://kvqa-aduit-application.onrender.com/view-kaf/${this.companyId}/${kaf}`,
    // //     "_blank"
    // //   );

    //     const fileUrl = `http://192.168.1.14:5000/view-kaf/${this.companyId}/${kaf}`;

    //     const viewerUrl = `https://docs.google.com/gview?url=${encodeURIComponent(fileUrl)}&embedded=true`;

    //     window.open(viewerUrl, "_blank");
    // },

    async viewFile(kaf) {
        try {
            const response = await axios.get(
            `https://kvqa-aduit-application.onrender.com/view-kaf/${this.companyId}/${kaf}`,
            { responseType: "blob" }
            );

            const blob = new Blob([response.data]);
            const url = window.URL.createObjectURL(blob);

            const link = document.createElement("a");
            link.href = url;

            // ✅ Get filename from backend
            const contentDisposition = response.headers['content-disposition'];
            let filename = `${kaf}.docx`;

            if (contentDisposition) {
            const match = contentDisposition.match(/filename="?(.+)"?/);
            if (match) filename = match[1];
            }

            link.download = filename;

            document.body.appendChild(link);
            link.click();
            link.remove();

        } catch (error) {
            console.error("Download failed:", error);
        }
    },

    openUpload(kaf) {
      this.selectedKaf = kaf;
      this.dialog = true;
    },

    async uploadFile() {
      if (!this.file) {
        alert("Please select a file");
        return;
      }

      const formData = new FormData();
      formData.append("file", this.file);

      try {
        await axios.post(
          `https://kvqa-aduit-application.onrender.com/upload-kaf/${this.companyId}/${this.selectedKaf}`,
          formData
        );

        this.dialog = false;
        this.file = null;
        this.fetchKAF(); // refresh
      } catch (error) {
        console.error("Upload error:", error);
      }
    }
  }
};
</script> -->


<!-- <template>
  <v-container>

    <v-card class="mb-4 pa-4">
      <v-card-title class="text-h5 font-weight-bold">
        {{ companyName || "Loading..." }}
      </v-card-title>
      <v-card-subtitle>
        KAF Document Tracking
      </v-card-subtitle>
    </v-card>

    <v-card>
      <v-card-title>KAF Details</v-card-title>

      <v-data-table :headers="headers" :items="kafList" class="mt-4">

        <template #[`item.action`]="{ item }">
          <v-btn 
            v-if="item.file_exists" 
            color="green" 
            @click="viewFile(item.kaf_type)">
            Download
          </v-btn>

          <v-btn 
            v-else 
            color="orange" 
            @click="openUpload(item.kaf_type)">
            Upload
          </v-btn>

        </template>

      </v-data-table>
    </v-card>

    <v-dialog v-model="dialog" width="400">
      <v-card>
        <v-card-title>Upload {{ selectedKaf }}</v-card-title>

        <v-card-text>
          <v-file-input v-model="file" label="Select File" />
        </v-card-text>

        <v-card-actions>
          <v-btn color="primary" @click="uploadFile">Upload</v-btn>
          <v-btn text @click="dialog = false">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      companyId: null,
      companyName: "",   // ✅ NEW
      kafList: [],
      headers: [
        { title: "KAF", key: "kaf_type" },
        { title: "Date", key: "date" },
        { title: "Action", key: "action" }
      ],
      dialog: false,
      selectedKaf: null,
      file: null
    };
  },

  mounted() {
    this.companyId = this.$route.params.companyId;

    if (this.companyId) {
      this.fetchKAF();
      this.fetchCompanyName();   // ✅ NEW
    } else {
      console.error("Company ID is undefined!");
    }
  },

  methods: {
    // ✅ Fetch KAF Status
    async fetchKAF() {
      try {
        const res = await axios.get(
          `https://kvqa-aduit-application.onrender.com/kaf-status/${this.companyId}`
        );
        this.kafList = res.data;
      } catch (error) {
        console.error("Error fetching KAF:", error);
      }
    },

    // ✅ Fetch Company Name (Optimized API)
    async fetchCompanyName() {
      try {
        const res = await axios.get(
          `https://kvqa-aduit-application.onrender.com/company/${this.companyId}`
        );
        this.companyName = res.data.name;
      } catch (error) {
        console.error("Error fetching company name:", error);
      }
    },

    // ✅ Download File
    async viewFile(kaf) {
      try {
        const response = await axios.get(
          `https://kvqa-aduit-application.onrender.com/view-kaf/${this.companyId}/${kaf}`,
          { responseType: "blob" }
        );

        const blob = new Blob([response.data]);
        const url = window.URL.createObjectURL(blob);

        const link = document.createElement("a");
        link.href = url;

        // Get filename from backend
        const contentDisposition = response.headers['content-disposition'];
        let filename = `${kaf}.docx`;

        if (contentDisposition) {
          const match = contentDisposition.match(/filename="?(.+)"?/);
          if (match) filename = match[1];
        }

        link.download = filename;

        document.body.appendChild(link);
        link.click();
        link.remove();

      } catch (error) {
        console.error("Download failed:", error);
      }
    },

    // ✅ Open Upload Dialog
    openUpload(kaf) {
      this.selectedKaf = kaf;
      this.dialog = true;
    },

    // ✅ Upload File
    async uploadFile() {
      if (!this.file) {
        alert("Please select a file");
        return;
      }

      const formData = new FormData();
      formData.append("file", this.file);

      try {
        await axios.post(
          `https://kvqa-aduit-application.onrender.com/upload-kaf/${this.companyId}/${this.selectedKaf}`,
          formData
        );

        this.dialog = false;
        this.file = null;
        this.fetchKAF(); // refresh table

      } catch (error) {
        console.error("Upload error:", error);
      }
    }
  }
};
</script> -->

<template>
  <v-container>

    <!-- Company Header -->
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

        <!-- Action Column -->
        <template #[`item.action`]="{ item }">

          <!-- If file exists → DOWNLOAD -->
          <v-btn 
            v-if="item.file_exists" 
            color="green" 
            @click="viewFile(item.kaf_type)">
            Download
          </v-btn>

          <!-- If no file → UPLOAD -->
          <v-btn 
            v-else 
            color="orange" 
            @click="openUpload(item.kaf_type)">
            Upload
          </v-btn>

        </template>

        <template #[`item.view`]="{ item }">
          <v-btn
            v-if="item.file_exists"
            color="purple"
            @click="viewUploadedFile(item.kaf_type)"
          >
            View
          </v-btn>

          <v-btn
            v-else
            color="grey"
            variant="outlined"
            disabled
          >
            Not Available
          </v-btn>
        </template>

        <!-- Send Mail Column -->
        <!-- Send Mail Column -->
        <template #[`item.mail`]="{ item }">

        <!-- Allowed → Active Button -->
        <v-btn
            v-if="allowedMailKAFs.includes(item.kaf_type)"
            :loading="item.sending"
            color="blue"
            @click="sendMail(item)"
        >
            {{ item.sent ? "Sent" : "Send Mail" }}
        </v-btn>

        <!-- Not Allowed → Disabled Button -->
        <v-btn
            v-else
            color="grey"
            variant="outlined"
            disabled
        >
            Not Applicable
        </v-btn>

        </template>

      </v-data-table>
    </v-card>

    <!-- Upload Dialog -->
    <v-dialog v-model="dialog" width="400">
      <v-card>
        <v-card-title>
          Upload {{ selectedKaf }}
        </v-card-title>

        <v-card-text>
          <v-file-input 
            v-model="file" 
            label="Select DOCX File"
            accept=".doc,.docx"
          />
        </v-card-text>

        <v-card-actions>
          <v-btn color="primary" @click="uploadFile">
            Upload
          </v-btn>
          <v-btn text @click="dialog = false">
            Cancel
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="previewDialog" width="900">
      <v-card>
        <v-card-title>
          Preview Document
        </v-card-title>

        <v-card-text style="max-height: 70vh; overflow-y: auto;">
          <div v-html="previewContent"></div>
        </v-card-text>

        <v-card-actions>
          <v-btn color="primary" @click="previewDialog = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </v-container>
</template>

<script>
import axios from "axios";
import mammoth from "mammoth";

export default {
  data() {
    return {
      companyId: null,
      companyName: "",

      // ✅ ALL KAF TYPES
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
      allowedMailKAFs: [
        "KAF1","KAF4","KAF5","KAF6","KAF7",
        "KAF8","KAF9","KAF10","KAF12",
        "KAF13","KAF19","KAF20"
      ],

      headers: [
        { title: "KAF", key: "kaf_name" },
        { title: "Date", key: "date" },
        { title: "Action", key: "action" },
        { title: "View", key: "view" },
        { title: "Send Mail", key: "mail" } 
      ],

      dialog: false,
      selectedKaf: null,
      file: null,
      previewDialog: false,
      previewContent: "",
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

    // ✅ Get Company Name
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

    // ✅ Merge backend data with master list
    async fetchKAF() {
      try {
        const res = await axios.get(
          `https://kvqa-aduit-application.onrender.com/kaf-status/${this.companyId}`
        );

        const backendData = res.data;

        // merge master + backend
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

    // ✅ Download file
    async viewFile(kaf) {
      try {
        const response = await axios.get(
          `https://kvqa-aduit-application.onrender.com/view-kaf/${this.companyId}/${kaf}`,
          { responseType: "blob" }
        );

        const blob = new Blob([response.data]);
        const url = window.URL.createObjectURL(blob);

        const link = document.createElement("a");
        link.href = url;

        // ✅ Custom filename
        link.download = `${this.companyName}_${kaf}.docx`;

        document.body.appendChild(link);
        link.click();
        link.remove();

      } catch (error) {
        console.error("Download failed:", error);
      }
    },

     async sendMail(item) {
        // Disable button temporarily (optional)
        item.sending = true;

        setTimeout(() => {
        item.sending = false;
        alert(`Mail sent for ${item.kaf_type}`);
        }, 1000);
    },

    openUpload(kaf) {
      this.selectedKaf = kaf;
      this.dialog = true;
    },

    async uploadFile() {
      if (!this.file) {
        alert("Please select a file");
        return;
      }

      const formData = new FormData();
      formData.append("file", this.file);

      try {
        await axios.post(
          `https://kvqa-aduit-application.onrender.com/upload-kaf/${this.companyId}/${this.selectedKaf}`,
          formData
        );

        this.dialog = false;
        this.file = null;

        this.fetchKAF(); // refresh

      } catch (error) {
        console.error("Upload error:", error);
      }
    },

    async viewUploadedFile(kaf) {
      try {
        const response = await axios.get(
          `https://kvqa-aduit-application.onrender.com/view-kaf/${this.companyId}/${kaf}`,
          { responseType: "arraybuffer" }
        );

        const result = await mammoth.convertToHtml({
          arrayBuffer: response.data
        });

        this.previewContent = result.value;
        this.previewDialog = true;

      } catch (error) {
        console.error("Preview failed:", error);
        alert("Unable to preview document.");
      }
    },
  }
};
</script>