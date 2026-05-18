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
        </v-list>
      </v-navigation-drawer>
  
      <v-main>
        <v-container>
          <v-form ref="form">
            <!-- Question 1 -->
            <v-col>
              <p>1. How is EMS preparation being organized?</p>
              <v-row class="d-flex align-center" style="gap: 50px;">
                <v-radio-group v-model="emsMethod" inline>
                  <v-radio label="In-house method" value="in-house"></v-radio>
                  <v-radio label="Consultancy method (including internal audit conducting agency)" value="consultancy"></v-radio>
                </v-radio-group>
              </v-row>
            </v-col>
  
            <!-- Conditional Fields for Consultancy method -->
            <v-row v-if="emsMethod === 'consultancy'">
              <v-col cols="12" md="4">
                <v-text-field v-model="consultingAgency" label="Consulting Agency" :rules="[requiredRule]" required></v-text-field>
              </v-col>
              <v-col cols="12" md="4">
                <v-text-field v-model="consultant" label="Consultant" :rules="[requiredRule]" required></v-text-field>
              </v-col>
              <v-col cols="12" md="4">
                <v-text-field v-model="consultingContractDate" label="Consulting Contract Date" type="date" :rules="[requiredRule]" required></v-text-field>
              </v-col>
            </v-row>
            <v-row v-if="emsMethod === 'in-house'">
                <v-col cols="12" md="4">
                    <v-text-field v-model="inHouseMethodDate" label="In-House Date" type="date" :rules="[requiredRule]" required></v-text-field>
                </v-col>
            </v-row>
            
            <!-- Separator Line -->
            <v-divider class="my-4"></v-divider>

            <!-- Question 2 -->
            <v-col>
                <p>2. Do you have any outsourced processes that affect conformity to product or service requirements?</p>
                <v-row class="d-flex align-center" style="gap: 50px;">
                    <v-radio-group v-model="outsourcedProcess" inline>
                        <v-radio label="Yes" value="yes"></v-radio>
                        <v-radio label="No" value="no"></v-radio>
                    </v-radio-group>
                </v-row>
            </v-col>

            <!-- Conditional Fields for Outsourced Processes -->
            <v-row v-if="outsourcedProcess==='yes'">
                <v-col cols="12" md="6">
                    <v-text-field v-model="region" label="Region" :rules="[requiredRule]" required></v-text-field>
                </v-col>
                <v-col cols="12" md="6">
                    <v-text-field v-model="processActivity" label="Process/Activity" :rules="[requiredRule]"required></v-text-field>
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
                <v-row class="d-flex align-center" style="gap: 50px;">
                    <v-radio-group v-model="duplicatedProcess" inline>
                        <v-radio label="Yes" value="yes"></v-radio>
                        <v-radio label="No" value="no"></v-radio>
                    </v-radio-group>
                </v-row>
            </v-col>

            <!-- Conditional Fields for Duplicated Process -->
            <v-row v-if="duplicatedProcess === 'yes'">
                <v-col cols="12" md="4">
                    <v-text-field v-model="numberofline" label="No. of Line:" :rules="[requiredRule]" required></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                    <v-text-field v-model="processname" label="Process Name:" :rules="[requiredRule]" required></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                    <v-text-field v-model="Numberofemployees" label="Number of employees:" :rules="[requiredRule]" required></v-text-field>
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
                <v-text-field v-model.number="shiftWorkers" label="No of shift workers" type="number" :rules="[requiredRule]" required></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                <v-text-field v-model.number="shiftPersons" label="Persons" type="number" :rules="[requiredRule]" required></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                <v-text-field v-model.number="shiftsPerDay" label="Shift/day" type="number" :rules="[requiredRule]" required></v-text-field>
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
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field v-model="manual" label="Manual" required></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field v-model="manualissuedate" label="manual issue date" type="date" :rules="[requiredRule]" required></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field v-model="procedure" label="Procedure" required></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field v-model="procedureissuedate" label="procedure issue date" type="date" :rules="[requiredRule]" required></v-text-field>
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

            <v-row class="d-flex align-center" style="gap: 50px;">
              <v-radio-group v-model="riskAnalysis" inline>
                <v-radio label="Yes" value="yes"></v-radio>
                <v-radio label="No" value="no"></v-radio>
              </v-radio-group>
            </v-row>

            <!-- Separator Line -->
            <v-divider class="my-4"></v-divider>

            <!-- Question 10 -->
            <v-row>
              <v-col cols="12">
                <p>10. Have you conducted Aspect & Impact Analysis related to EMS </p>
              </v-col>
            </v-row>

            <v-row class="d-flex align-center" style="gap: 50px;">
              <v-radio-group v-model="impactAnalysis" inline>
                <v-radio label="Yes" value="yes"></v-radio>
                <v-radio label="No" value="no"></v-radio>
              </v-radio-group>
            </v-row>

            <!-- Separator Line -->
            <v-divider class="my-4"></v-divider>

            <!-- Question 11 -->

            <v-col>
                <p>11. Have you ever received the same certification audit from other certification agency? </p>
                <v-row class="d-flex align-center" style="gap: 50px;">
                  <v-radio-group v-model="certificationAudit" inline>
                    <v-radio label="Yes" value="yes"></v-radio>
                    <v-radio label="No" value="no"></v-radio>
                  </v-radio-group>
                </v-row>
            </v-col>

            <!-- Conditional Fields for Duplicated Process -->
            <v-row v-if="certificationAudit==='yes'">
              <v-col cols="12" md="6">
                <v-text-field v-model="nameofagency" label="Name of Agency:" :rules="[requiredRule]" required></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field v-model="time" label="Time" type= "date" :rules="[requiredRule]" required></v-text-field>
              </v-col>
            </v-row>

            <!-- Separator Line -->
            <v-divider class="my-4"></v-divider>

            <!-- Question 12 -->
            <v-col>
                <p>12. Do you have any other certified system including environmental friendly enterprise certification? </p>
                <v-row class="d-flex align-center" style="gap: 50px;">
                  <v-radio-group v-model="environmentCertification" inline>
                    <v-radio label="Yes" value="yes"></v-radio>
                    <v-radio label="No" value="no"></v-radio>
                  </v-radio-group>
                </v-row>
            </v-col>

            <!-- Conditional Fields for Environment Certification Process -->

            <v-row v-if="environmentCertification==='yes'">
              <v-col cols="12" md="4">
                <v-text-field v-model="certificationstadard" label="Certification Standard" :rules="[requiredRule]" required></v-text-field>
              </v-col>
              <v-col cols="12" md="4">
                <v-text-field v-model="certificationagency" label="Certification Agency" :rules="[requiredRule]" required></v-text-field>
              </v-col>
              <v-col cols="12" md="4">
                <v-text-field v-model="acquisitiondate" label="Acquisition Date" type="date" :rules="[requiredRule]" required></v-text-field>
              </v-col>
            </v-row>

            <!-- Separator Line -->
            <v-divider class="my-4"></v-divider>

            <!-- Question 13 -->
            <v-col>
              <p>13. Have you ever had an environmental accident occurred in the last 3 years? </p>
              <v-row class="d-flex align-center" style="gap: 50px;">
                <v-radio-group v-model="environmentaccident" inline>
                  <v-radio label="Yes" value="yes"></v-radio>
                  <v-radio label="No" value="no"></v-radio>
                </v-radio-group>
              </v-row>
              <v-textarea v-if="environmentaccident.includes('yes')" v-model="accidentNote" label="If yes, please describe it briefly" required></v-textarea>
              <p>Note: When mfg. industry, please fill out No13~14, when construction/supervision industry, please fill out No.</p>
            </v-col>

            <!-- Conditional Fields for Environment Accident -->
            <v-row v-if="environmentaccident==='yes'">
              <v-col cols="12" md="6">
                <v-text-field v-model="accidentdate" label="Accident Date" type="date" :rules="[requiredRule]" required min="2011-01-01" max="2050-12-31"></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field v-model="accidenttype" label="Accident Type" :rules="[requiredRule]" required></v-text-field>
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

            <v-row class="d-flex align-center" style="gap: 50px;">
              <v-radio-group v-model="manufacturingmethod" inline>
                <v-radio label="Simple Fabrication" value="simplefabrication" :disabled="!environmentaccident.includes('yes')"></v-radio>
                <v-radio label="Chemical Treatment" value="chemicaltreatment" :disabled="!environmentaccident.includes('yes')"></v-radio>
                <v-radio label="Automatic Manufacturing System" value="automaticmanufacturingsystem" :disabled="!environmentaccident.includes('yes')"></v-radio>
                <v-radio label="Other Leather Product" value="otherleatherproduct" :disabled="!environmentaccident.includes('yes')"></v-radio>
              </v-radio-group>
            </v-row>

            <!-- Separator Line -->
            <v-divider class="my-4"></v-divider>

            <!-- Question 15 -->

            <v-row>
              <v-col cols="12">
                <p>15. What are your conditions of location? </p>
              </v-col>
            </v-row>

            <v-row class="d-flex align-center" style="gap: 50px;">
              <v-radio-group v-model="locationcondition" inline>
                <v-radio label="Special Measure's Zone" value="specialmeasurezone"></v-radio>
                <v-radio label="Water Supply Source Protection Zone" value="watersupplyzone"></v-radio>
                <v-radio label="Industrial Estate" value="industrialestate"></v-radio>
                <v-radio label="Residential" value="residential"></v-radio>
                <v-radio label="Country" value="country"></v-radio>
                <v-radio label="Others" value="others"></v-radio>
              </v-radio-group>
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
                <v-row class="d-flex align-center" style="gap: 50px;">
                  <v-radio-group v-model="wasteGas" inline>
                    <v-radio label="Residential" value="residential"></v-radio>
                    <v-radio label="Industrial" value="industrial"></v-radio>
                    <v-radio label="Semi Urban" value="semi-urban"></v-radio>
                  </v-radio-group>
                </v-row>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <p>ii) Waste water effluence facility permission</p>
                <v-row class="d-flex align-center" style="gap: 50px;">
                  <v-radio-group v-model="wasteWater" inline>
                    <v-radio label="Residential" value="residential"></v-radio>
                    <v-radio label="Industrial" value="industrial"></v-radio>
                    <v-radio label="Semi Urban" value="semi-urban"></v-radio>
                  </v-radio-group>
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
                <v-row class="d-flex align-center" style="gap: 50px;">
                  <v-radio-group v-model="noxiousChemicals" inline>
                    <v-radio label="Applicable" value="applicable"></v-radio>
                    <v-radio label="N/A" value="na"></v-radio>
                  </v-radio-group>
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
                <v-row class="d-flex align-center" style="gap: 50px;">
                  <v-radio-group v-model="businessType" inline>
                    <v-radio label="Civil" value="civil"></v-radio>
                    <v-radio label="Architecture" value="architecture"></v-radio>
                    <v-radio label="Plant" value="plant"></v-radio>
                    <v-radio label="Construction Material" value="construction-material"></v-radio>
                    <v-radio label="Specialty Construction" value="specialty-construction"></v-radio>
                  </v-radio-group>
                  </v-row>
              </v-col>
            </v-row>
            
            <!-- Sub-question 3 -->
            <v-row>
              <v-col cols="12" md="4">
                <v-text-field v-model.number="numSites" label="No. of Sites" type="number" :rules="[requiredRule]" required></v-text-field>
              </v-col>
              <v-col cols="12" md="8">
                <v-text-field v-model="siteLocations" label="Location of Sites" :rules="[requiredRule]" required></v-text-field>
              </v-col>
            </v-row>

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

          </v-form>
  
          <!-- Submit Button -->
          <v-btn @click="submitForm" color="primary" :disabled="!isFormValid">Submit</v-btn>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        emsMethod: '',
        consultingAgency: '',
        consultant: '',
        consultingContractDate: '',
        inHouseMethodDate: '',
        outsourcedProcess: '',
        region: '',
        processActivity: '',
        processes: [],
        duplicatedProcess: '',
        numberofline: '',
        processname: '',
        Numberofemployees: '',
        shiftWorkers: 0,
        shiftPersons: 0,
        shiftsPerDay: 0,
        manual: '',
        manualissuedate: '',
        procedure: '',
        procedureissuedate: '',
        internalAuditDate: '',
        managementReviewDate: '',
        certificationAuditDate: '',
        riskAnalysis: '',
        impactAnalysis: '',
        certificationAudit: '',
        nameofagency: '',
        time: '',
        environmentCertification: '',
        certificationstadard: '',
        certificationagency: '',
        acquisitiondate: '',
        environmentaccident: '',
        accidentNote: '',
        accidentdate: '',
        accidenttype: '',
        manufacturingmethod: '',
        locationcondition: '',
        wasteGas: '',
        wasteWater: '',
        wasteAmount: 0,
        noxiousChemicals: '',
        pollutionBoardConsent: 0,
        certificationNumber: 0,
        businessType: '',
        numSites: 0,
        siteLocations: '',
        siteField: '',
        siteNumber: 0,
        siteAddress: '',
        signedBy: '',
        designation: '',
        director: '',
        finaldate: '',
        requiredRule: v => !!v || 'This field is required' // Validation rule
      };
    },
    computed: {
      isFormValid() {
        if (!this.emsMethod) {
          return false;
        }
        if (this.emsMethod === 'consultancy' && (!this.consultingAgency.trim() || !this.consultant.trim() || !this.consultingContractDate.trim())) {
          return false;
        }
        if (this.emsMethod === 'in-house' && !this.inHouseMethodDate.trim()) {
            return false;
        }
        if (!this.outsourcedProcess) {
            return false;
        }
        if (this.outsourcedProcess === 'yes' && (!this.region.trim() || !this.processActivity.trim())) {
            return false;
        }
        if (!this.duplicatedProcess) {
            return false;
        }
        if (this.duplicatedProcess === 'yes' && (!this.numberofline.trim() || !this.processname.trim() || !this.Numberofemployees.trim())) {
            return false;
        }

        if (!this.shiftWorkers || !this.shiftPersons || !this.shiftsPerDay) {
          return false;
        }

        if (!this.manual || !this.manualissuedate || !this.procedure || !this.procedureissuedate) {
          return false;
        }

        if (!this.internalAuditDate || !this.managementReviewDate || !this.certificationAuditDate || !this.riskAnalysis) {
          return false;
        }

        if (!this.riskAnalysis) {
          return false;
        }

        if (!this.impactAnalysis) {
          return false;
        }

        if (!this.certificationAudit) {
          return false;
        }

        if (this.certificationAudit === 'yes' && (!this.nameofagency.trim() || !this.time.trim())) {
          return false;
        }

        if (!this.environmentCertification) {
          return false;
        }

        if (this.environmentCertification === 'yes' && (!this.certificationstadard.trim() || !this.certificationagency.trim() || !this.acquisitiondate.trim())) {
          return false;
        }

        if (!this.environmentaccident) {
          return false;
        }

        if (this.environmentaccident === 'yes' && (!this.accidentNote.trim() || !this.accidentdate.trim() || !this.accidenttype.trim() || !this.manufacturingmethod)) {
          return false;
        }

        if (!this.locationcondition) {
          return false;
        }

        if (!this.wasteGas || !this.wasteWater || !this.wasteAmount || !this.noxiousChemicals) {
          return false;
        }

        if (!this.pollutionBoardConsent || !this.certificationNumber || !this.businessType || !this.numSites || !this.siteLocations) {
          return false;
        }

        return true;
        // return this.emsMethod !== '' && this.outsourcedProcess !== ''; // Must select at least one method
      }
    },
    methods: {
      submitForm() {
        if (!this.isFormValid) {
          alert("Please fill all required fields.");
          return;
        }
  
        const formData = {
          emsMethod: this.emsMethod,
          consultingAgency: this.consultingAgency,
          consultant: this.consultant,
          consultingContractDate: this.consultingContractDate,
          inHouseMethodDate: this.inHouseMethodDate,
          outsourcedProcess: this.outsourcedProcess,
          region: this.region,
          processActivity: this.processActivity,
          processes: this.processes,
          duplicatedProcess: this.duplicatedProcess,
          numberofline: this.numberofline,
          processname: this.processname,
          Numberofemployees: this.Numberofemployees,
          shiftWorkers: this.shiftWorkers,
          shiftPersons: this.shiftPersons,
          shiftsPerDay: this.shiftsPerDay,
          manual: this.manual,
          manualissuedate: this.manualissuedate,
          procedure: this.procedure,
          procedureissuedate: this.procedureissuedate,
          internalAuditDate: this.internalAuditDate,
          managementReviewDate: this.managementReviewDate,
          certificationAuditDate: this.certificationAuditDate,
          riskAnalysis: this.riskAnalysis,
          impactAnalysis: this.impactAnalysis,
          certificationAudit: this.certificationAudit,
          nameofagency: this.nameofagency,
          time: this.time,
          environmentCertification: this.environmentCertification,
          certificationstadard: this.certificationstadard,
          certificationagency: this.certificationagency,
          acquisitiondate: this.acquisitiondate,
          environmentaccident: this.environmentaccident,
          accidentNote: this.accidentNote,
          accidentdate: this.accidentdate,
          accidenttype: this.accidenttype,
          manufacturingmethod: this.manufacturingmethod,
          locationcondition: this.locationcondition,
          wasteGas: this.wasteGas,
          wasteWater: this.wasteWater,
          wasteAmount: this.wasteAmount,
          noxiousChemicals: this.noxiousChemicals,
          pollutionBoardConsent: this.pollutionBoardConsent,
          certificationNumber: this.certificationNumber,
          businessType: this.businessType,
          numSites: this.numSites,
          siteLocations: this.siteLocations
        };
  
        axios.post('https://kvqa-aduit-application.onrender.com/ems_submit', formData)
          .then(response => {
            console.log(response);
          })
          .catch(error => {
            console.log(error);
          });
      }
    }
  };
  </script>