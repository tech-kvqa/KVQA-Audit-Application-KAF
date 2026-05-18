<!-- <template>
    <v-app>
        <v-container>
            <v-card class="pa-5">
                <v-card-title>Contract Review Report</v-card-title>
                <v-card-text>
                <v-text-field label="Organization" v-model="form.organization"></v-text-field>
                <v-text-field label="Quotation No." v-model="form.quotationNo"></v-text-field>
                <v-text-field label="Address" v-model="form.address"></v-text-field>
                
                <v-radio-group v-model="form.application" label="Application">
                    <v-radio label="Initial Audit" value="initial"></v-radio>
                    <v-radio label="Renewal Audit" value="renewal"></v-radio>
                </v-radio-group>
                
                <v-text-field label="Contract No." v-model="form.contractNo"></v-text-field>
                
                <v-select label="Size" v-model="form.size" :items="['Small', 'Medium', 'Large']"></v-select>
                
                <v-text-field label="No. of Employees" v-model="form.noOfEmployees" type="number"></v-text-field>
                <v-text-field label="Effective No. of Employees" v-model="form.effectiveNoOfEmployees" type="number"></v-text-field>
                
                <v-checkbox v-model="form.auditStandards" label="ISO 9001:2015" value="ISO 9001:2015"></v-checkbox>
                <v-checkbox v-model="form.auditStandards" label="ISO 14001:2015" value="ISO 14001:2015"></v-checkbox>
                <v-checkbox v-model="form.auditStandards" label="ISO 45001:2018" value="ISO 45001:2018"></v-checkbox>
                <v-checkbox v-model="form.auditStandards" label="ISO 27001:2013" value="ISO 27001:2013"></v-checkbox>
                <v-checkbox v-model="form.auditStandards" label="ISO 20000-1:2018" value="ISO 20000-1:2018"></v-checkbox>
                
                <v-text-field label="IAF Code" v-model="form.iafCode"></v-text-field>
                <v-text-field label="Complexity" v-model="form.complexity"></v-text-field>
                <v-text-field label="Audit Scope" v-model="form.auditScope"></v-text-field>
                
                <v-select label="On-site Type" v-model="form.onSiteType" :items="['Multi-site', 'Single site', 'Temporary site']"></v-select>
                
                <v-text-field label="Tentative Audit Schedule - Stage 1" v-model="form.stage1"></v-text-field>
                <v-text-field label="Tentative Audit Schedule - Stage 2" v-model="form.stage2"></v-text-field>
                
                <v-btn color="primary" @click="submitForm">Submit</v-btn>
                </v-card-text>
            </v-card>
        </v-container>
    </v-app>
  </template>
  
  <script>
  export default {
    data() {
      return {
        form: {
          organization: '',
          quotationNo: '',
          address: '',
          application: '',
          contractNo: '',
          size: '',
          noOfEmployees: '',
          effectiveNoOfEmployees: '',
          auditStandards: [],
          iafCode: '',
          complexity: '',
          auditScope: '',
          onSiteType: '',
          stage1: '',
          stage2: ''
        }
      };
    },
    methods: {
      submitForm() {
        console.log(this.form);
      }
    }
  };
  </script>
  
-->


<template>
    <v-container>
      <v-card class="pa-5">
        <v-card-title>Contract Review Report</v-card-title>
        <v-card-text>
          <v-form>
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field label="Organization" v-model="form.organization" required></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field label="Quotation No." v-model="form.quotationNo" required></v-text-field>
              </v-col>
            </v-row>
            
            <v-row>
              <v-col cols="12">
                <v-text-field label="Address" v-model="form.address" required></v-text-field>
              </v-col>
            </v-row>
            <!-- <v-row>
              <v-col cols="12" md="6">
                <v-select
                  label="Application"
                  v-model="form.application"
                  :items="['Initial Audit', 'Renewal Audit']"
                ></v-select>
              </v-col>
            </v-row> -->

            <v-row align="center">
                <v-col cols="12" md="3">
                    <label>Application:</label>
                </v-col>
                <v-col cols="12" md="4">
                    <v-checkbox v-model="form.initial" label="Initial Audit" value="Initial Audit" multiple density="compact" hide-details></v-checkbox>
                </v-col>
                <v-col cols="12" md="4">
                    <v-checkbox
                    v-model="form.renewal"
                    label="Renewal Audit"
                    value="Renewal Audit"
                    multiple
                    density="compact"
                    hide-details
                    ></v-checkbox>
                </v-col>
            </v-row>
            
            <v-row>
              <v-col cols="12" md="6">
                <v-select
                  label="Size"
                  v-model="form.size"
                  :items="['Small', 'Medium', 'Large']"
                ></v-select>
              </v-col>
              <v-col cols="12" md="3">
                <v-text-field label="No. of Employees" v-model="form.employees" type="number" required></v-text-field>
              </v-col>
              <v-col cols="12" md="3">
                <v-text-field label="Effective No. of Employees" v-model="form.employees_effetcive" type="number" required></v-text-field>
              </v-col>
            </v-row>
            
            <!-- <v-row>
              <v-col cols="12">
                <v-checkbox-group v-model="form.auditStandards" label="Audit Standards">
                  <v-checkbox value="ISO 9001:2015" label="ISO 9001:2015"></v-checkbox>
                  <v-checkbox value="ISO 14001:2015" label="ISO 14001:2015"></v-checkbox>
                  <v-checkbox value="ISO 45001:2018" label="ISO 45001:2018"></v-checkbox>
                  <v-checkbox value="ISO 27001:2013" label="ISO 27001:2013"></v-checkbox>
                  <v-checkbox value="ISO 20000-1:2018" label="ISO 20000-1:2018"></v-checkbox>
                </v-checkbox-group>
              </v-col>
            </v-row> -->

            <v-row align="center">
                <v-col cols="12" md="2">
                    <label>Audit Standards:</label>
                </v-col>
                <v-col cols="12" md="10" class="d-flex flex-wrap">
                    <v-checkbox
                        v-model="form.auditStandards"
                        value="ISO 9001:2015"
                        label="ISO 9001:2015"
                        density="compact"
                        hide-details
                    ></v-checkbox>
                    <v-checkbox
                        v-model="form.auditStandards"
                        value="ISO 14001:2015"
                        label="ISO 14001:2015"
                        density="compact"
                        hide-details
                    ></v-checkbox>
                    <v-checkbox
                        v-model="form.auditStandards"
                        value="ISO 45001:2018"
                        label="ISO 45001:2018"
                        density="compact"
                        hide-details
                    ></v-checkbox>
                    <v-checkbox
                        v-model="form.auditStandards"
                        value="ISO 27001:2013"
                        label="ISO 27001:2013"
                        density="compact"
                        hide-details
                    ></v-checkbox>
                    <v-checkbox
                        v-model="form.auditStandards"
                        value="ISO 20000-1:2018"
                        label="ISO 20000-1:2018"
                        density="compact"
                        hide-details
                    ></v-checkbox>
                </v-col>
            </v-row>
            
            <v-row>
              <v-col cols="12" md="6">
                <v-text-field label="IAF Code" v-model="form.iafCode"></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-select
                  label="Complexity"
                  v-model="form.complexity"
                  :items="['High', 'Medium', 'Low']"
                ></v-select>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12">
                <v-text-field label="Audit Scope" v-model="form.auditScope"></v-text-field>
              </v-col>
            </v-row>
            
            <!-- <v-row>
              <v-col cols="12">
                <v-select
                  label="On-site Type"
                  v-model="form.onSiteType"
                  :items="['Multi-site', 'Single site', 'Temporary site']"
                ></v-select>
              </v-col>
            </v-row> -->

            <v-row align="center">
                <v-col cols="12" md="3">
                    <label>On-site Type:</label>
                </v-col>
                <v-col cols="12" md="3">
                    <v-checkbox 
                        v-model="form.multiSite" 
                        label="Multi-site" 
                        value="Multi-site" 
                        multiple 
                        density="compact" 
                        hide-details
                    ></v-checkbox>
                </v-col>
                <v-col cols="12" md="3">
                    <v-checkbox
                        v-model="form.singleSite"
                        label="Single Site"
                        value="Single Site"
                        multiple
                        density="compact"
                        hide-details
                    ></v-checkbox>
                </v-col>
                <v-col cols="12" md="3">
                    <v-checkbox
                        v-model="form.temporarySite"
                        label="Temporary Site"
                        value="Temporary Site"
                        multiple
                        density="compact"
                        hide-details
                    ></v-checkbox>
                </v-col>
            </v-row>

            <v-row>
                <!-- Fixed md=6 for Tentative Audit Schedule -->
                <v-col cols="12" md="2">
                <!-- <v-card>
                    <v-card-title>Tentative Audit Schedule</v-card-title>
                </v-card> -->
                    <label>Tentative Audit Schedule</label>
                </v-col>

                <!-- Fixed md=10 for the rest -->
                <v-col cols="12" md="10">
                <v-row>
                    <!-- Stage 1 Audit -->
                    <v-col cols="12" md="4">
                    <v-text-field
                        label="Stage 1 Audit Date"
                        v-model="form.stage1AuditDate"
                        type="date"
                    ></v-text-field>
                    </v-col>
                    
                    <!-- Any Other Audit -->
                    <v-col cols="12" md="4">
                    <v-text-field
                        label="Any Other Audit Date"
                        v-model="form.anyOtherAuditDate"
                        type="date"
                    ></v-text-field>
                    </v-col>

                    <!-- Stage 2 Audit -->
                    <v-col cols="12" md="4">
                    <v-text-field
                        label="Stage 2 Audit Date"
                        v-model="form.stage2AuditDate"
                        type="date"
                    ></v-text-field>
                    </v-col>
                </v-row>

                <!-- <v-table>
                    <thead>
                    <tr>
                        <th>Audit Type</th>
                        <th>Days</th>
                        <th>Fee</th>
                        <th>Total Fee</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>Document Audit</td>
                        <td><v-text-field v-model="form.docAuditDays" type="number"></v-text-field></td>
                        <td><v-text-field v-model="form.docAuditFee" type="number"></v-text-field></td>
                        <td>{{ form.docAuditDays * form.docAuditFee }}</td>
                    </tr>
                    <tr>
                        <td>Pre-audit</td>
                        <td><v-text-field v-model="form.preAuditDays" type="number"></v-text-field></td>
                        <td><v-text-field v-model="form.preAuditFee" type="number"></v-text-field></td>
                        <td>{{ form.preAuditDays * form.preAuditFee }}</td>
                    </tr>
                    <tr>
                        <td>On-site Audit</td>
                        <td><v-text-field v-model="form.onsiteAuditDays" type="number"></v-text-field></td>
                        <td><v-text-field v-model="form.onsiteAuditFee" type="number"></v-text-field></td>
                        <td>{{ form.onsiteAuditDays * form.onsiteAuditFee }}</td>
                    </tr>
                    </tbody>
                </v-table>

                <v-row>
                    <v-col cols="12" md="6">
                    <v-text-field
                        label="Calculation"
                        v-model="form.calculation"
                        readonly
                    ></v-text-field>
                    </v-col>
                    <v-col cols="12" md="6">
                    <v-text-field
                        label="Signature"
                        v-model="form.signature"
                    ></v-text-field>
                    </v-col>
                </v-row>
                </v-col> -->
                <!-- Audit Fee Table -->
                <v-table>
                <thead>
                    <tr>
                    <th>Audit Type</th>
                    <th>Days</th>
                    <th>Fee</th>
                    <th>Total Fee</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <td>Document Audit</td>
                    <td><v-text-field v-model="form.docAuditDays" type="number"></v-text-field></td>
                    <td><v-text-field v-model="form.docAuditFee" type="number"></v-text-field></td>
                    <td>{{ form.docAuditDays * form.docAuditFee }}</td>
                    </tr>
                    <tr>
                    <td>Pre-audit</td>
                    <td><v-text-field v-model="form.preAuditDays" type="number"></v-text-field></td>
                    <td><v-text-field v-model="form.preAuditFee" type="number"></v-text-field></td>
                    <td>{{ form.preAuditDays * form.preAuditFee }}</td>
                    </tr>
                    <tr>
                    <td>On-site Audit</td>
                    <td><v-text-field v-model="form.onsiteAuditDays" type="number"></v-text-field></td>
                    <td><v-text-field v-model="form.onsiteAuditFee" type="number"></v-text-field></td>
                    <td>{{ form.onsiteAuditDays * form.onsiteAuditFee }}</td>
                    </tr>
                </tbody>
                </v-table>

                <!-- Fee Breakdown (2 per 3 yrs, 3 per 3 yrs, 5 per 3 yrs) -->
                <v-row>
                <v-col cols="12" md="4">
                    <v-text-field label="2 per 3 yrs Fee" v-model="form.twoPerThreeFee" type="number"></v-text-field>
                    <v-text-field label="Total" v-model="form.twoPerThreeTotal" readonly></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                    <v-text-field label="3 per 3 yrs Fee" v-model="form.threePerThreeFee" type="number"></v-text-field>
                    <v-text-field label="Total" v-model="form.threePerThreeTotal" readonly></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                    <v-text-field label="5 per 3 yrs Fee" v-model="form.fivePerThreeFee" type="number"></v-text-field>
                    <v-text-field label="Total" v-model="form.fivePerThreeTotal" readonly></v-text-field>
                </v-col>
                </v-row>

                <!-- Calculation and Signature -->
                <v-row>
                <v-col cols="12" md="6">
                    <v-text-field label="Calculation (Total number of md(s))" v-model="form.calculation" readonly></v-text-field>
                </v-col>
                <v-col cols="12" md="3">
                    <v-text-field label="Signature" v-model="form.signature"></v-text-field>
                </v-col>
                <v-col cols="12" md="3">
                    <v-text-field label="Date" v-model="form.date" type="date"></v-text-field>
                </v-col>
                </v-row>
            </v-col>
            </v-row>
            
            <v-divider class="my-4"></v-divider>
            <v-btn color="primary" @click="submitForm">Submit</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        form: {
          organization: '',
          quotationNo: '',
          address: '',
          initial: '',
          renewal: '',
          size: '',
          employees: '',
          auditStandards: [],
          iafCode: '',
          auditScope: '',
          onSiteType: '',
          stage1: '',
          stage2: '',
          employees_effetcive: '',
          complexity: '',
          multiSite: '',
          singleSite: '',
          temporarySite: '',
          stage1Date: "",
        docAuditDays: "",
        docAuditFee: "",
        preAuditDays: "",
        preAuditFee: "",
        onSiteAuditDays: "",
        onSiteAuditFee: "",
        totalFee: "",
        stage2: "",
        stage2Date: "",
        stage2Fee: "",
        signature: "",
        signatureDate: "",
        },
      };
    },
    methods: {
      submitForm() {
        console.log('Form Submitted:', this.form);
      },
    },
  };
  </script>
  
  <style scoped>
  </style>
  