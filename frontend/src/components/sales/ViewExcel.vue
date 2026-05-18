<!-- <template>
    <v-container>
      <v-btn color="primary" class="mb-4" @click="$router.push('/sales/dashboard')">
        Back to Dashboard
      </v-btn>
  
      <v-card v-if="excelData">
        <v-card-title>Excel File: {{ companyName }} - {{ questionnaireType }}</v-card-title>
        <v-card-text>
          <v-simple-table dense>
            <thead>
              <tr>
                <th v-for="(col, index) in excelData[0]" :key="index">
                  {{ col }}
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, rowIndex) in excelData.slice(1)" :key="rowIndex">
                <td v-for="(cell, cellIndex) in row" :key="cellIndex">
                  {{ cell }}
                </td>
              </tr>
            </tbody>
          </v-simple-table>
        </v-card-text>
      </v-card>
  
      <v-alert v-else type="error">Failed to load the file.</v-alert>
    </v-container>
  </template>
  
  <script>
  import * as XLSX from "xlsx";
  import axios from "axios";
  
  export default {
    data() {
      return {
        excelData: null,
        companyName: this.$route.params.companyName,
        questionnaireType: this.$route.params.questionnaireType
      };
    },
    async mounted() {
      await this.fetchExcelFile();
    },
    methods: {
      async fetchExcelFile() {
        try {
          const response = await axios.get(
            `https://kvqa-audit-application-kaf.onrender.com/sales/get-uploaded-form/${this.companyName}/${this.questionnaireType}`,
            { responseType: "arraybuffer" }
          );
  
          const workbook = XLSX.read(response.data, { type: "array" });
          const sheetName = workbook.SheetNames[0];
          const sheet = workbook.Sheets[sheetName];
          this.excelData = XLSX.utils.sheet_to_json(sheet, { header: 1 });
        } catch (error) {
          console.error("Error fetching Excel file:", error);
        }
      }
    }
  };
  </script>
   -->


   <template>
    <!-- <v-container>
      <v-btn color="primary" class="mb-4" @click="$router.push('/sales/dashboard')">
        Back to Dashboard
      </v-btn>
  
      <v-card v-if="excelData.length">
        <v-card-title>Excel File: {{ companyName }} - {{ questionnaireType }}</v-card-title>
        <v-card-text>
          <hot-table
            :data="excelData"
            :colHeaders="true"
            :rowHeaders="true"
            :licenseKey="'non-commercial-and-evaluation'"
            class="excel-table"
          ></hot-table>
        </v-card-text>
      </v-card>
  
      <v-alert v-else type="error">Failed to load the file.</v-alert>
    </v-container> -->
    <v-container>
  <v-btn color="primary" class="mb-4" @click="$router.push('/sales/application')">
    Back to Dashboard
  </v-btn>

  <v-card v-if="excelData.length > 0">
    <v-card-title>Excel File: {{ companyName }} - {{ questionnaireType }}</v-card-title>
    <v-card-text>
      <hot-table
        v-if="excelData.length > 0"
        :data="excelData.map(row => row.map(cell => cell || ''))"
        :colHeaders="excelHeaders"
        :rowHeaders="true"
        :stretchH="'all'"
        :width="'100%'"
        :height="'auto'"
        :columns="[
          { width: 50 },                   // Column 1: #
          { width: dynamicColumnWidth },    // Column 2: Particulars (Dynamic Width)
          { width: 200 }                    // Column 3: Answer
        ]"
        :wordWrap="true"
        :licenseKey="'non-commercial-and-evaluation'"
        class="excel-table"
      ></hot-table>

      <v-alert v-else type="warning">
        Data is empty or incorrectly formatted.
      </v-alert>
    </v-card-text>
  </v-card>

  <v-alert v-else type="error">Failed to load the file.</v-alert>
</v-container>


  </template>
  
  <script>
  import * as XLSX from "xlsx";
  import axios from "axios";
  import { HotTable } from "@handsontable/vue3";
  import "handsontable/dist/handsontable.full.css";
  
  export default {
    components: { HotTable },
    data() {
      return {
        excelData: [],
        companyName: this.$route.params.companyName,
        questionnaireType: this.$route.params.questionnaireType
      };
    },
    async mounted() {
      console.log("Mounted: Handsontable should render.");
      await this.fetchExcelFile();
    },
    methods: {
    //   async fetchExcelFile() {
    //     try {
    //       const response = await axios.get(
    //         `https://kvqa-audit-application-kaf.onrender.com/sales/get-uploaded-form/${this.companyName}/${this.questionnaireType}`,
    //         { responseType: "arraybuffer" }
    //       );
  
    //       const workbook = XLSX.read(response.data, { type: "array" });
    //       const sheetName = workbook.SheetNames[0];
    //       const sheet = workbook.Sheets[sheetName];
    //       this.excelData = XLSX.utils.sheet_to_json(sheet, { header: 1, blankrows: false });
    //     } catch (error) {
    //       console.error("Error fetching Excel file:", error);
    //     }
    //   }

    async fetchExcelFile() {
  try {
    console.log("Fetching Excel file...");
    const response = await axios.get(
      // `https://kvqa-audit-application-kaf.onrender.com/sales/get-uploaded-form/${this.companyName}/${this.questionnaireType}`,
      `https://kvqa-audit-application-kaf.onrender.com/sales/get-uploaded-form/${this.companyName}/${this.questionnaireType}`,
      { responseType: "arraybuffer" }
    );

    console.log("Response received:", response);

    // Convert ArrayBuffer to Uint8Array
    const data = new Uint8Array(response.data);
    const workbook = XLSX.read(data, { type: "array" });

    // Get first sheet
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];

    // Convert sheet to JSON (raw data)
    const rawData = XLSX.utils.sheet_to_json(sheet, { header: 1, blankrows: false });

    console.log("Raw Excel Data:", rawData);

    if (rawData.length > 1) {
      let headers = rawData[1];
      while (headers.length < 3) {
        // headers.push(`Column ${headers.length + 1}`); // Fill missing headers
        headers.push(` `); // Fill missing headers
      }
      this.excelHeaders = headers;

      // Extract data (skip first 2 rows)
      this.excelData = rawData.slice(2);
    } else {
      this.excelHeaders = ["#", "Particulars", "Answer"];  // Default headers if missing
      this.excelData = [];
    }

    // Calculate the max width for "Particulars" column dynamically
    let maxTextLength = 0;
    this.excelData.forEach(row => {
      if (row[1] && row[1].length > maxTextLength) {
        maxTextLength = row[1].length;
      }
    });

    // Convert character length to pixels (approx. 8px per character)
    this.dynamicColumnWidth = Math.min(50 + maxTextLength * 8, 600); // Limit max width to 600px

    console.log("Extracted Headers:", this.excelHeaders);
    console.log("Formatted Excel Data:", this.excelData);
  } catch (error) {
    console.error("Error fetching Excel file:", error);
  }
}



    }
  };
  </script>
  
  <style>
  .excel-table {
    width: 100%;
    height: 600px;
  }
  </style>
  