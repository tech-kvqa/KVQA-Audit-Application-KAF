<template>
  <v-app>
    <!-- Sidebar Navigation Drawer -->
    <v-navigation-drawer app>
      <v-list>
        <v-list-item link to="/consultant/dashboard">
          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item link to="/consultant/application">
          <v-list-item-content>
            <v-list-item-title>Application</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <!-- <v-list-item @click="logout">
          <v-list-item-content>
            <v-list-item-title class="text-red">Logout</v-list-item-title>
          </v-list-item-content>
        </v-list-item> -->
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <v-container>
        <v-form ref="form">
          <!-- Question 1 -->
          <v-col>
            <p>1. How is EMS preparation being organized?</p>
            <v-row>
                <v-checkbox v-model="emsMethod" label="In-house method" value="in-house"></v-checkbox>
                <v-spacer class="small-spacer"></v-spacer>
                <v-checkbox v-model="emsMethod" label="Consultancy method (including internal audit conducting agency)" value="consultancy" density="compact"></v-checkbox>
            </v-row>
          </v-col>

          <!-- Conditional Fields for Consultancy method -->
          <v-row v-if="emsMethod.includes('consultancy')">
            <v-col cols="12" md="4">
              <v-text-field v-model="consultingAgency" label="Consulting Agency" required></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="consultant" label="Consultant" required></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="consultingContractDate" label="Consulting Contract Date" type="date" required></v-text-field>
            </v-col>
          </v-row>

          <!-- Separator Line -->
          <v-divider class="my-4"></v-divider>

          <!-- Question 2 -->
          <v-col>
              <p>2. Do you have any outsourced processes that affect conformity to product or service requirements?</p>
              <v-row>
                <v-checkbox v-model="outsourcedProcess" label="Yes" value="yes"></v-checkbox>
                <v-spacer class="small-spacer"></v-spacer>
                <v-checkbox v-model="outsourcedProcess" label="No" value="no"></v-checkbox>
            </v-row>
          </v-col>

          <!-- Conditional Fields for Outsourced Processes -->
          <v-row v-if="outsourcedProcess.includes('yes')">
            <v-col cols="12" md="6">
              <v-text-field v-model="region" label="Region" required></v-text-field>
            </v-col>
            <v-col cols="12" md="6">
              <v-text-field v-model="processActivity" label="Process/Activity" required></v-text-field>
            </v-col>
          </v-row>

          <!-- Separator Line -->
          <v-divider class="my-4"></v-divider>

          <!-- Question 3 -->
          <v-row>
            <v-col cols="12">
              <p>3. Please list down the Key Processes involved relevant to the Management system?</p>
              <v-btn @click="addProcess" :disabled="processes.length >= 5" class="mb-2">Add Process</v-btn>
            </v-col>
          </v-row>
          
          <v-row v-for="(process, index) in processes" :key="index">
            <v-col cols="12" md="10">
              <v-text-field v-model="processes[index]" label="Process" required></v-text-field>
            </v-col>
            <v-col cols="12" md="2">
              <v-btn @click="removeProcess(index)" color="red">Remove</v-btn>
            </v-col>
          </v-row>

          <!-- Separator Line -->
          <v-divider class="my-4"></v-divider>

          <!-- Question 4 -->
          <v-col>
              <p>4. Do you have any duplicated process?</p>
              <v-row>
                <v-checkbox v-model="duplicatedProcess" label="Yes" value="yes"></v-checkbox>
                <v-spacer class="small-spacer"></v-spacer>
                <v-checkbox v-model="duplicatedProcess" label="No" value="no"></v-checkbox>
              </v-row>
          </v-col>

          <!-- Conditional Fields for Duplicated Process -->
          <v-row v-if="duplicatedProcess.includes('yes')">
            <v-col cols="12" md="4">
              <v-text-field v-model="numberofline" label="No. of Line:" required></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="processname" label="Process Name:" required></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="Numberofemployees" label="Number of employees:" required></v-text-field>
            </v-col>
          </v-row>

          <!-- Separator Line -->
          <v-divider class="my-4"></v-divider>

          <!-- Question 5 -->
          <v-row>
            <v-col cols="12">
              <p>5. What is your shift work’s status?</p>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="4">
              <v-text-field v-model.number="shiftWorkers" label="No of shift workers" type="number" required></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model.number="shiftPersons" label="Persons" type="number" required></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model.number="shiftsPerDay" label="Shift/day" type="number" required></v-text-field>
            </v-col>
          </v-row>

          <!-- Separator Line -->
          <v-divider class="my-4"></v-divider>

          <!-- Question 6 -->

          <v-row>
            <v-col cols="12">
              <p>6. What’s your system’s structure? </p>
            </v-col>
          </v-row>

          <!-- Separator Line -->
          <v-divider class="my-4"></v-divider>

          <!-- Question 7 -->
          <v-row>
            <v-col cols="12">
              <p>7. When did you conduct internal audit and management review (or planned)? </p>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="12" md="6">
              <v-text-field v-model="internalAuditDate" label="Internal Audit Date" type="date" required></v-text-field>
            </v-col>
            <v-col cols="12" md="6">
              <v-text-field v-model="managementReviewDate" label="Management Review Date" type="date" required></v-text-field>
            </v-col>
          </v-row>
          
          <!-- Separator Line -->
          <v-divider class="my-4"></v-divider>

          <!-- Question 8 -->

          <v-row>
            <v-col cols="12">
              <p>8. When do you want the certification audit conducted? </p>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="12">
              <v-text-field v-model="certificationAuditDate" label="Certification Audit Date" type="date" required></v-text-field>
            </v-col>
          </v-row>

          <!-- Separator Line -->
          <v-divider class="my-4"></v-divider>

          <!-- Question 9 -->
          <v-row>
            <v-col cols="12">
              <p>9. Have you conducted EMS (ISO 14001:2015) Related Risk Analysis? </p>
            </v-col>
          </v-row>

          <v-row>
              <v-checkbox v-model="riskAnalysis" label="Yes" value="yes"></v-checkbox>
              <v-spacer class="small-spacer"></v-spacer>
              <v-checkbox v-model="riskAnalysis" label="No" value="no"></v-checkbox>
          </v-row>

          <!-- Separator Line -->
          <v-divider class="my-4"></v-divider>

          <!-- Question 10 -->
          <v-row>
            <v-col cols="12">
              <p>10. Have you conducted Aspect & Impact Analysis related to EMS </p>
            </v-col>
          </v-row>

          <v-row>
              <v-checkbox v-model="impactAnalysis" label="Yes" value="yes"></v-checkbox>
              <v-spacer class="small-spacer"></v-spacer>
              <v-checkbox v-model="impactAnalysis" label="No" value="no"></v-checkbox>
          </v-row>

          <!-- Separator Line -->
          <v-divider class="my-4"></v-divider>

          <!-- Question 11 -->

          <v-col>
              <p>11. Have you ever received the same certification audit from other certification agency? </p>
              <v-row>
                <v-checkbox v-model="certificationAudit" label="Yes" value="yes"></v-checkbox>
                <v-spacer class="small-spacer"></v-spacer>
                <v-checkbox v-model="certificationAudit" label="No" value="no"></v-checkbox>
              </v-row>
          </v-col>

          <!-- Conditional Fields for Duplicated Process -->
          <v-row v-if="certificationAudit.includes('yes')">
            <v-col cols="12" md="6">
              <v-text-field v-model="nameofagency" label="Name of Agency:" required></v-text-field>
            </v-col>
            <v-col cols="12" md="6">
              <v-text-field v-model="time" label="Time" required></v-text-field>
            </v-col>
          </v-row>

          <!-- Separator Line -->
          <v-divider class="my-4"></v-divider>

          <!-- Question 12 -->
          <v-col>
              <p>12. Do you have any other certified system including environmental friendly enterprise certification? </p>
              <v-row>
                <v-checkbox v-model="environmentCertification" label="Yes" value="yes"></v-checkbox>
                <v-spacer class="small-spacer"></v-spacer>
                <v-checkbox v-model="environmentCertification" label="No" value="no"></v-checkbox>
              </v-row>
          </v-col>

          <!-- Conditional Fields for Environment Certification Process -->

          <v-row v-if="environmentCertification.includes('yes')">
            <v-col cols="12" md="4">
              <v-text-field v-model="certificationstadard" label="Certification Standard" required></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="certificationagency" label="Certification Agency" required></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="acquisitiondate" label="Acquisition Date" type="date" required></v-text-field>
            </v-col>
          </v-row>

          <!-- Separator Line -->
          <v-divider class="my-4"></v-divider>

          <!-- Question 13 -->
          <v-col>
            <p>13. Have you ever had an environmental accident occurred in the last 3 years? </p>
            <v-row>
              <v-checkbox v-model="environmentaccident" label="Yes" value="yes"></v-checkbox>
              <v-spacer class="small-spacer"></v-spacer>
              <v-checkbox v-model="environmentaccident" label="No" value="no"></v-checkbox>
            </v-row>
            <v-textarea v-if="environmentaccident.includes('yes')" v-model="accidentNote" label="If yes, please describe it briefly" required></v-textarea>
            <p>Note: When mfg. industry, please fill out No13~14, when construction/supervision industry, please fill out No.</p>
          </v-col>

          <!-- Conditional Fields for Environment Accident -->
          <v-row v-if="environmentaccident.includes('yes')">
            <v-col cols="12" md="6">
              <v-text-field v-model="accidentdate" label="Accident Date" type="date" required min="2011-01-01" max="2050-12-31"></v-text-field>
            </v-col>
            <v-col cols="12" md="6">
              <v-text-field v-model="accidenttype" label="Accident Type" required></v-text-field>
            </v-col>
          </v-row>

          <!-- Separator Line -->
          <v-divider class="my-4"></v-divider>

          <!-- Question 14 -->
          <v-row>
            <v-col cols="12">
              <p>14. What is your manufacturing method? </p>
            </v-col>
          </v-row>

          <v-row>
            <v-checkbox v-model="manufacturingmethod" label="Simple Fabrication" value="simplefabrication" :disabled="!environmentaccident.includes('yes')"></v-checkbox>
            <v-checkbox v-model="manufacturingmethod" label="Chemical Treatment" value="chemicaltreatment" :disabled="!environmentaccident.includes('yes')"></v-checkbox>
            <v-checkbox v-model="manufacturingmethod" label="Automatic Manufacturing System" value="automaticmanufacturingsystem" :disabled="!environmentaccident.includes('yes')"></v-checkbox>
            <v-checkbox v-model="manufacturingmethod" label="Other Leather Product" value="otherleatherproduct" :disabled="!environmentaccident.includes('yes')"></v-checkbox>
          </v-row>

          <!-- Separator Line -->
          <v-divider class="my-4"></v-divider>

          <!-- Question 15 -->

          <v-row>
            <v-col cols="12">
              <p>15. What are your conditions of location? </p>
            </v-col>
          </v-row>

          <v-row>
              <v-checkbox v-model="locationcondition" label="Special Measure's Zone" value="specialmeasurezone"></v-checkbox>
              <v-checkbox v-model="locationcondition" label="Water Supply Source Protection Zone" value="watersupplyzone"></v-checkbox>
              <v-checkbox v-model="locationcondition" label="Industrial Estate" value="industrialestate"></v-checkbox>
              <v-checkbox v-model="locationcondition" label="Residential" value="residential"></v-checkbox>
              <v-checkbox v-model="locationcondition" label="Country" value="country"></v-checkbox>
              <v-checkbox v-model="locationcondition" label="Others" value="others"></v-checkbox>
          </v-row>

          <!-- Separator Line -->
          <v-divider class="my-4"></v-divider>

          <!-- Question 16 -->
          <v-row>
            <v-col cols="12">
              <p>16. What is your environmental load Air & water consent pollution control board? </p>
            </v-col>
          </v-row>
          
            <v-row>
            <v-col cols="12">
              <p>i) Waste gas emission facility permission</p>
              <v-row>
                <v-col>
                  <v-checkbox v-model="wasteGas" label="Residential" value="residential"></v-checkbox>
                </v-col>
                <v-col>
                  <v-checkbox v-model="wasteGas" label="Industrial" value="industrial"></v-checkbox>
                </v-col>
                <v-col>
                  <v-checkbox v-model="wasteGas" label="Semi Urban" value="semi-urban"></v-checkbox>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <p>ii) Waste water effluence facility permission</p>
              <v-row>
                <v-col>
                  <v-checkbox v-model="wasteWater" label="Residential" value="residential"></v-checkbox>
                </v-col>
                <v-col>
                  <v-checkbox v-model="wasteWater" label="Industrial" value="industrial"></v-checkbox>
                </v-col>
                <v-col>
                  <v-checkbox v-model="wasteWater" label="Semi Urban" value="semi-urban"></v-checkbox>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="6">
              <p>iii) Waste amount (Ton/yr)</p>
              <v-text-field v-model.number="wasteAmount" type="number" required></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <p>iv) Noxious chemicals use permission</p>
              <v-row>
                  <v-checkbox v-model="noxiousChemicals" label="Applicable" value="applicable"></v-checkbox>
                  <v-spacer class="small-spacer"></v-spacer>
                  <v-checkbox v-model="noxiousChemicals" label="N/A" value="na"></v-checkbox>
              </v-row>
            </v-col>
          </v-row>
          
          <!-- Separator Line -->
          <v-divider class="my-4"></v-divider>

          <!-- Question 17 -->
          <v-row>
            <v-col cols="12">
              <p>17.</p>
            </v-col>
          </v-row>
          <!-- Sub-question 1 -->
          <v-row class="align-center">
            <v-col cols="12" class="d-flex align-center text-field-row">
              <p>i) No of Pollution Board Consent:</p>
              <v-text-field v-model.number="pollutionBoardConsent" label="Enter Number" type="number" dense single-line required class="small-text-field mx-2"></v-text-field>
              <p>kinds</p>
              <v-spacer class="small-spacer"></v-spacer>
              <p>No of Certification:</p>
              <v-text-field v-model.number="certificationNumber" label="Enter Number" type="number" dense single-line required class="small-text-field mx-2"></v-text-field>
              <p>kinds</p>
            </v-col>
          </v-row>
      
          <!-- Sub-question 2 -->
          <v-row>
            <v-col cols="12">
              <p>ii) Type of Business:</p>
              <v-row>
                <v-col>
                  <v-checkbox v-model="businessType" label="Civil" value="civil"></v-checkbox>
                </v-col>
                <v-col>
                  <v-checkbox v-model="businessType" label="Architecture" value="architecture"></v-checkbox>
                </v-col>
                <v-col>
                  <v-checkbox v-model="businessType" label="Plant" value="plant"></v-checkbox>
                </v-col>
                <v-col>
                  <v-checkbox v-model="businessType" label="Construction Material" value="construction-material"></v-checkbox>
                </v-col>
                <v-col>
                  <v-checkbox v-model="businessType" label="Specialty Construction" value="specialty-construction"></v-checkbox>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
          
          <!-- Sub-question 3 -->
          <v-row>
            <v-col cols="12" md="4">
              <v-text-field v-model.number="numSites" label="No. of Sites" type="number" required></v-text-field>
            </v-col>
            <v-col cols="12" md="8">
              <v-text-field v-model="siteLocations" label="Location of Sites" required></v-text-field>
            </v-col>
          </v-row>
        </v-form>
        <!-- Table Outside the Form -->
    <v-table class="mt-6" bordered>
      <thead>
        <tr>
          <th>Name of site/field</th>
          <th>No of site</th>
          <th>Location/Address</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><v-text-field v-model="siteField" label="Enter Name" dense></v-text-field></td>
          <td><v-text-field v-model="siteNumber" label="Enter Number" type="number" dense></v-text-field></td>
          <td><v-textarea v-model="siteAddress" label="Enter Address" dense></v-textarea></td>
        </tr>
      </tbody>
    </v-table>

    <v-table class="mt-6" bordered>
      <tbody>
        <tr>
          <td>Signed By:</td>
          <td><v-text-field v-model="signedBy" label="Enter Name" dense></v-text-field></td>
          <td>Designation:</td>
          <td><v-text-field v-model="designation" label="Enter Designation" dense></v-text-field></td>
        </tr>
        <tr>
          <td>Director</td>
          <td><v-text-field v-model="director" label="Enter Name" dense></v-text-field></td>
          <td>Date:</td>
          <td><v-text-field v-model="finaldate" label="Enter Date" type="date" dense></v-text-field></td>
        </tr>
      </tbody>
    </v-table>

    <!-- Submit Button -->
    <v-btn @click="submitForm" color="primary">Submit</v-btn>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      emsMethod: [],
      consultingAgency: '',
      consultant: '',
      consultingContractDate: '',
      outsourcedProcess: [],
      region: '',
      processActivity: '',
      processes: [],
      duplicatedProcess: [],
      numberofline: '',
      processname: '',
      Numberofemployees: '',
      shiftWorkers: '',
      shiftPersons: '',
      shiftsPerDay: '',
      internalAuditDate: '',
      managementReviewDate: '',
      certificationAuditDate: '',
      riskAnalysis: [],
      impactAnalysis: [],
      certificationAudit: [],
      nameofagency: '',
      time: '',
      environmentCertification: [],
      certificationstadard: '',
      certificationagency: '',
      acquisitiondate: '',
      environmentaccident: [],
      accidentdate: null,
      accidenttype: '',
      accidentNote: '',
      manufacturingmethod: [],
      locationcondition: [],
      environmentalload: '',
      wasteGas: [],
      wasteWater: [],
      wasteAmount: '',
      noxiousChemicals: [],
      pollutionBoardConsent: '',
      certificationNumber: '',
      businessType: [],
      numSites: '',
      siteLocations: '',
      siteField: '',
      siteNumber: '',
      siteAddress: '',
      signedBy: '',
      designation: '',
      director: '',
      finaldate: '',
      menu: false
    };
  },

  methods: {
    addProcess() {
      this.processes.push('');
    },

    removeProcess(index) {
      this.processes.splice(index, 1);
    },

    async submitForm() {
  try {
    const response = await axios.post("https://kvqa-audit-application-kaf.onrender.com/qms_submit", this.formData, {
      headers: {
        "Content-Type": "application/json" // Ensure JSON format
      }
    });
    console.log("Data stored successfully", response.data);
  } catch (error) {
    console.error("Error storing data:", error.response ? error.response.data : error);
  }
},
  }
};
</script>
  
<style scoped>
.checkbox-group {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.small-text-field {
  max-width: 100px;
}
.text-field-row {
  display: flex;
  align-items: center;
  gap: 8px;
}
.mx-2 {
  margin-left: 8px;
  margin-right: 8px;
}
.small-spacer {
  flex-grow: 0.1; /* Reduce the spacing effect */
}
</style>