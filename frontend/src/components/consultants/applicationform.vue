<template>
    <v-app>
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
        <h2 class="text-h5 font-weight-bold text-center">Questionnaire</h2>
        <h3 class="text-subtitle-1 text-center font-italic">
          For Quality/Environment/Occupational Health Safety/Food Safety Management System/ 
          Information Security Management Certification (A)
          (Common Purpose)
        </h3>
  
        <v-divider class="my-5"></v-divider>
  
        <!-- Organization & Representative Details -->
        <v-table dense>
          <thead>
            <tr>
              <th>Name of Organization</th>
              <th>Director</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><v-text-field v-model="form.organization"></v-text-field></td>
              <td><v-text-field v-model="form.director"></v-text-field></td>
            </tr>
          </tbody>
  
          <thead>
            <tr>
              <th colspan="2">Address</th>
            </tr>
          </thead>
          <tbody>
            <!-- <tr>
              <td colspan="2"><v-textarea v-model="form.address"></v-textarea></td>
            </tr> -->
            <tr>
              <td colspan="2">
                <v-textarea v-model="form.address"></v-textarea>
              </td>
            </tr>
            <tr v-for="(unit, index) in additionalUnits" :key="index">
              <td colspan="2">
                <v-text-field v-model="additionalUnits[index]" label="Additional Unit Address"></v-text-field>
              </td>
            </tr>
          </tbody>

          <!-- Add More Units Button -->
          <v-btn
            color="primary"
            class="mt-2"
            @click="addUnit"
            :disabled="additionalUnits.length >= 3"
          >
            Add More Units
          </v-btn>
  
          <thead>
            <tr>
              <th>Environmental Management Representative</th>
              <th>Contact Details</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <v-text-field label="Name of Dept" v-model="form.department"></v-text-field>
                <v-text-field label="Title/Name" v-model="form.title"></v-text-field>
              </td>
              <td>
                <v-text-field label="Telephone" v-model="form.tel"></v-text-field>
                <v-text-field label="Email" v-model="form.email"></v-text-field>
              </td>
            </tr>
          </tbody>
        </v-table>
  
        <!-- Employee Details -->
        <h3 class="text-h6 mt-4">Number of Employees</h3>
        <v-table dense>
          <thead>
            <tr>
              <th>Executive</th>
              <th>Contractual/Temporary</th>
              <th>Part-Time</th>
              <th>Repetitive Process</th>
              <th>Shift</th>
              <th>Permanent</th>
              <th>Any Other</th>
              <th>Total</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><v-text-field v-model.number="form.executives" type="number"></v-text-field></td>
              <td><v-text-field v-model.number="form.contractual" type="number"></v-text-field></td>
              <td><v-text-field v-model.number="form.partTime" type="number"></v-text-field></td>
              <td><v-text-field v-model.number="form.repetitive" type="number"></v-text-field></td>
              <td><v-text-field v-model.number="form.shift" type="number"></v-text-field></td>
              <td><v-text-field v-model.number="form.permanent" type="number"></v-text-field></td>
              <td><v-text-field v-model.number="form.anyother" type="number"></v-text-field></td>
              <!-- <td><v-text-field :value="totalEmployees" type="number" readonly></v-text-field></td> -->
              <td><v-text-field v-model="form.total" type="number" readonly></v-text-field></td>
            </tr>
          </tbody>
        </v-table>

        <!-- Details of Manpower at each Site -->
        <h3 class="text-h6 mt-4">Details of Manpower at Each Site</h3>

        <!-- Checkbox for More Than One Site -->
        <v-radio-group v-model="form.hasMultipleSites" row>
          <v-radio label="Yes" value="yes"></v-radio>
          <v-radio label="No" value="no"></v-radio>
        </v-radio-group>

        <!-- Manpower Details - Show Only If "Yes" is Selected -->
        <template v-if="form.hasMultipleSites === 'yes'">
          <v-text-field 
            v-model="form.manpowerDetails[0]" 
            label="Enter manpower details for site 1"
          ></v-text-field>

          <v-row v-for="(site, index) in form.additionalSites" :key="index">
            <v-col cols="10">
              <v-text-field 
                v-model="form.additionalSites[index]" 
                :label="'Enter manpower details for site ' + (index + 2)"
              ></v-text-field>
            </v-col>
            <v-col cols="2">
              <v-btn 
                color="red" 
                icon 
                @click="removeSite(index)"
              >
                <v-icon>mdi-delete</v-icon>
              </v-btn>
            </v-col>
          </v-row>

          <!-- Add More Sites Button -->
          <v-btn 
            color="primary" 
            class="mt-2" 
            @click="addSite" 
            :disabled="form.additionalSites.length >= 2"
          >
            + Add More Sites
          </v-btn>
        </template>
  
        <!-- Certification Standards -->
        <h3 class="text-h6 mt-4">Certification Standards</h3>

        <!-- <v-row>
            <v-col v-for="(standard, key) in form.standards" :key="key" cols="2">
                <v-checkbox v-model="form.standards[key].value" :label="standard.label"></v-checkbox>
            </v-col>
        </v-row> -->

        <v-radio-group v-model="form.selectedStandard">
          <v-row>
            <v-col v-for="(label, key) in form.standards" :key="key" cols="2">
              <v-radio :label="label" :value="label"></v-radio>
            </v-col>
          </v-row>
        </v-radio-group>
  
        <!-- Expecting Scope of Certification -->
        <h3 class="text-h6 mt-4">Expecting Scope of Certification</h3>
        <h3 class="text-subtitle-1 text-center font-italic">
            Certification scope determines the characters of business and activities controlled by your 
            management system and can be used as a basis of description of certificate.
        </h3>
        <v-text-field label="Certification Site" v-model="form.certificationSite"></v-text-field>
        <v-textarea label="Scope" v-model="form.scope"></v-textarea>
  
        <h4 class="text-subtitle-1">Activities</h4>
        <v-row>
          <v-col v-for="(activity, key) in form.activities" :key="key" cols="3">
            <v-checkbox v-model="form.activities[key].value" :label="activity.label"></v-checkbox>
          </v-col>
        </v-row>
        <v-text-field label="If Others, specify" v-if="form.activities.others" v-model="form.otherActivity"></v-text-field>
  
        <!-- Multi-Site Certification Conditions -->
        <h3 class="text-h6 mt-4">Certification Conditions for Multi-Site</h3>
        <v-row>
            <v-col cols="12">
                <v-radio-group v-model="form.multiSite.orgStructure" label="Are all sites organized under the same organization?">
                <template v-slot:default>
                    <v-radio label="Yes" value="yes"></v-radio>
                    <v-radio label="No" value="no"></v-radio>
                </template>
                </v-radio-group>

                <v-radio-group v-model="form.multiSite.managementSystem" label="Are all sites operated under the same management system?">
                <template v-slot:default>
                    <v-radio label="Yes" value="yes"></v-radio>
                    <v-radio label="No" value="no"></v-radio>
                </template>
                </v-radio-group>

                <v-radio-group v-model="form.multiSite.internalAudit" label="Are all internal audit & management reviews conducted comprehensively?">
                <template v-slot:default>
                    <v-radio label="Yes" value="yes"></v-radio>
                    <v-radio label="No" value="no"></v-radio>
                </template>
                </v-radio-group>
            </v-col>
        </v-row>

        <!-- Audit Desired -->
        <h3 class="text-h6 mt-4">Audit Desired</h3>
        <v-row>
            <v-col cols="12">
                <v-radio-group v-model="form.audit.desired">
                    <template v-slot:label>
                        <v-label>Surveillance Audit</v-label>
                    </template>
                    <v-radio label="6 Monthly (5 times in 3 years)" value="6_monthly_5_times"></v-radio>
                    <v-radio label="Six Monthly first then yearly (3 times in 3 years)" value="6_monthly_then_yearly"></v-radio>
                    <v-radio label="Yearly (2 times per 3 years)" value="yearly_2_times"></v-radio>
                </v-radio-group>
            </v-col>
        </v-row>

        <!-- Additional Comments -->
        <h3 class="text-h6 mt-4">Anything specific you would like to convey on QMS/EMS/FSMS/OHSAS</h3>
        <v-textarea v-model="form.audit.comments" label="Enter your comments here..." outlined></v-textarea>

        <!-- Contact Information -->
        <!-- <v-alert type="info" variant="outlined" class="mt-4">
        <strong>📩 If you have any questions about filling out the questionnaire, don’t hesitate to contact us:</strong><br />
        <strong>Address:</strong> KVQA CERTIFICATION SERVICES PRIVATE LIMITED <br />
        F-300, Sector-63, Noida-201301, U.P. India <br />
        <strong>Phone:</strong> +91 98100 59955 <br />
        <strong>Email:</strong> <a href="mailto:delhi@kvqaindia.com">delhi@kvqaindia.com</a>
        </v-alert> -->

  
        <v-btn color="primary" class="mt-5" @click="submitForm">Submit</v-btn>
        <v-btn color="primary" class="mt-5" @click="navigatetoquestionnairepage">Move to Questionnaire Page</v-btn>
      </v-container>
    </v-main>
    </v-app>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        form: {
          organization: "",
          director: "",
          address: "",
          department: "",
          emr: "",
          tel: "",
          title: "",
          email: "",
          executives: 0,
          contractual: 0,
          partTime: 0,
          repetitive: 0,
          shift: 0,
          permanent: 0,
          anyother: 0,
          total: 0,
          certificationSite: "",
          scope: "",
          selectedStandard: "",
          // standards: {
          //   iso9001: { label: "ISO 9001:2015", value: false },
          //   iso14001: { label: "ISO 14001:2015", value: false },
          //   iso45001: { label: "ISO 45001:2018", value: false },
          //   iso27001: { label: "ISO 27001:2022", value: false },
          //   iso22000: { label: "ISO 22000:2018", value: false },
          // },
          standards: {
            iso9001: "ISO 9001:2015",
            iso14001: "ISO 14001:2015",
            iso45001: "ISO 45001:2018",
            iso27001: "ISO 27001:2022",
            iso22000: "ISO 22000:2018",
          },
          activities: {
            design: { label: "Design/Development", value: false },
            manufacturing: { label: "Manufacturing", value: false },
            installation: { label: "Installation", value: false },
            construction: { label: "Construction", value: false },
            sales: { label: "Sales", value: false },
            service: { label: "Service", value: false },
            others: { label: "Others", value: false },
          },
          otherActivity: "",
          multiSite: {
            orgStructure: "",
            managementSystem: "",
            internalAudit: "",
          },
          audit: {
            desired: "",
            comments: ""
          },
          hasMultipleSites: "no",  // Default to "No"
          manpowerDetails: [""],   // First site input
          additionalSites: [],     // Additional site inputs (max 2)
        },
        additionalUnits: [],
      };
    },
    methods: {
      async submitForm() {
        try {
          const payload = {
            organization: this.form.organization,
            director: this.form.director,
            address: this.form.address,
            department: this.form.department,
            emr: this.form.emr,
            tel: this.form.tel,
            title: this.form.title,
            email: this.form.email,
            executives: this.form.executives,
            contractual: this.form.contractual,
            partTime: this.form.partTime,
            repetitive: this.form.repetitive,
            shift: this.form.shift,
            permanent: this.form.permanent,
            anyother: this.form.anyother,
            total: this.form.total,
            certificationSite: this.form.certificationSite,
            scope: this.form.scope,
            standards: Object.keys(this.form.standards).filter(key => this.form.standards[key].value),
            activities: Object.keys(this.form.activities).filter(key => this.form.activities[key].value),
            otherActivity: this.form.otherActivity,
            multiSite: this.form.multiSite,
            audit: this.form.audit,
            hasMultipleSites: this.form.hasMultipleSites,
            manpowerDetails: this.form.manpowerDetails,
            additionalSites: this.form.additionalSites
          };

          const response = await axios.post("https://kvqa-audit-application-kaf.onrender.com/submit", payload);
          
          if (response.status === 200) {
            alert("Form submitted successfully!");
            console.log("Response:", response.data);
          }
        } catch (error) {
          console.error("Error submitting form:", error);
          alert("Failed to submit form. Please try again.");
        }
      },

      navigatetoquestionnairepage() {
        this.$router.push('/consultant/questionnaire');
      },

      addUnit() {
        if (this.additionalUnits.length < 3) {
          this.additionalUnits.push("");
        }
      },

      addSite() {
      if (this.form.additionalSites.length < 2) {
        this.form.additionalSites.push("");
      }
    },
    removeSite(index) {
      this.form.additionalSites.splice(index, 1);
    },

      totalEmployees() {
        return this.form.executives + this.form.contractual + this.form.partTime + this.form.repetitive + this.form.shift + this.form.permanent + this.form.anyother;
      }
    },

    watch: {
      // Watch all form fields and update total dynamically
      form: {
        handler() {
          this.form.total =
            (parseInt(this.form.executives) || 0) +
            (parseInt(this.form.contractual) || 0) +
            (parseInt(this.form.partTime) || 0) +
            (parseInt(this.form.repetitive) || 0) +
            (parseInt(this.form.shift) || 0) +
            (parseInt(this.form.permanent) || 0) +
            (parseInt(this.form.anyother) || 0);
        },
        deep: true,
        immediate: true,
      },
    },
  };
  </script>
  