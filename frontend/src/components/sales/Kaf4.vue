<!-- <template>
    <v-container>
      <v-card class="pa-5">
        <v-card-title class="text-h5 text-center">Certification Audit Contract</v-card-title>
        
        <v-row>
          <v-col cols="12">
            <v-text-field label="Company Name" v-model="companyName"></v-text-field>
          </v-col>
        </v-row>
  
        <v-row>
          <v-col cols="12">
            <v-textarea label="Site 1 Address" v-model="site1"></v-textarea>
          </v-col>
          <v-col cols="12">
            <v-text-field label="Scope" v-model="scope1"></v-text-field>
          </v-col>
        </v-row>
  
        <v-row>
          <v-col cols="12">
            <v-textarea label="Site 2 Address" v-model="site2"></v-textarea>
          </v-col>
          <v-col cols="12">
            <v-text-field label="Scope" v-model="scope2"></v-text-field>
          </v-col>
        </v-row>
        
        <v-divider></v-divider>
        
        <v-row>
          <v-col cols="12">
            <h3>Article 1: Objective of contract</h3>
            <p>This contract is for both the applicant and the certification body to observe all the necessary rights and duties for each of them in performing certification audit applied by the applicant.</p>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col cols="12">
            <h3>Article 2: Scope of certification</h3>
            <p>The certification body assesses and certifies/registers the applicant’s Quality/Environmental Management System for products, activities and services provided its sites concerned, with respect to Quality/Environmental Management System standards and any supplementation required.</p>
          </v-col>
        </v-row>
        
        <v-btn color="primary" @click="submitForm">Submit</v-btn>
      </v-card>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        companyName: '',
        site1: '',
        scope1: '',
        site2: '',
        scope2: ''
      };
    },
    methods: {
      submitForm() {
        console.log("Form submitted", this.$data);
      }
    }
  };
  </script>
   -->


   <template>
    <v-container>
      <v-card class="pa-5">
        <!-- <v-card-title class="text-h5">Certification Audit Contract</v-card-title> -->
        <!-- <v-card-subtitle>( Company Name ) & KVQA ASSESSMENT PRIVATE LIMITED</v-card-subtitle>
        <v-divider class="my-3"></v-divider> -->
        
        <v-row>
          <v-col cols="12" md="9">
            <p><strong>Doc. No:</strong> KAF-04</p>
          </v-col>
          <v-col cols="12" md="3">
            <p><strong>Form:</strong> 2023.01</p>
          </v-col>
        </v-row>
        <v-divider></v-divider>
        <v-card-title class="text-h5" align="center">Certification Audit Contract</v-card-title>
        <v-row>
          <v-col cols="12" md="6">
            <p><strong>Site 1:</strong> (Address)</p>
            <p><strong>Scope:</strong> (Description)</p>
            <p><strong>Site 2:</strong> (Additional Scope)</p>
          </v-col>
        </v-row>
        
        <v-divider class="my-3"></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title>Article 1: Objective of Contract</v-card-title>
            <v-card-text>
              <p>This contract is for both the applicant and the certification body to observe all the necessary rights and duties for each of them in performing certification audit applied by the applicant.</p>
            </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title>Article 2: Scope of Certification</v-card-title>
          <v-card-text>
            <p>The certification body assesses and certifies/registers the applicant’s Quality/Environmental Management System for products, activities and services provided its sites concerned, with the respect to Quality/Environmental Management System standards and any supplementation required under the system.  The scope of certification/registration can be changed as to activities actual audit performed. The standard for the certification shall be ISO 14001:2015. The total man-day spent shall be…3...man-days (stage 1…. 1Mandays & Stage 2-…2Man-days) Annual Surveillance …1…Man-days</p>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">
            Article 3: Certification Audit
          </v-card-title>
          <v-card-text class="text-body-1">
            <p>
              Certification audit is performed on the basis of audit standards and Quality/Environmental Management of the applicant. The Accreditation body may visit for certification activities along with KVQA ASSESSMENT PRIVATE LIMITED or otherwise:
            </p>
            <v-list density="compact">
              <v-list-item>
                <v-list-item-content>
                  <p class="text-body-1">
                    <strong>1. </strong> Document audit of the applicant’s QMS/EMS documents and records is carried out, prior to on-site audit. QMS/EMS documents include Manual, procedures, work instructions, report of internal audit, data of management review, and data for identifying environmental aspects etc.
                  </p>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <p class="text-body-1">
                    <strong>2. </strong> Pre-audit is performed upon the applicant’s request in accordance with certification procedures. Pre-audit is not to determine but to evaluate the conformity of its relevant QMS/EMS/OHMS/ISMS.
                  </p>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <p class="text-body-1">
                    <strong>3. </strong> On-site Audit is performed at the applicant's sites to evaluate if its activities are implemented according to documented system. If non-conformities are found during audit, the certification body issues CAR (corrective action request).
                  </p>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <p class="text-body-1">
                    <strong>4. </strong> When non-conformities are found with the result of the audit, registration of certification is determined through certification deliberation, after conducting document or on-site follow-up audit.
                  </p>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <p class="text-body-1">
                    <strong>5. </strong> The certification body provides its applicants with documented compliance requirements for maintaining its certification/registration, when certificate is granted.
                  </p>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <p class="text-body-1">
                    <strong>6. </strong> The accreditation body can visit your premises.
                  </p>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 4: The confirmation of the Certification standard</v-card-title>
          <v-card-text>
            <p>The confirmation of the certification scope Certification standard, certification scope (items) and address of on-sites are decided with prior mutual agreement. Ambiguities relating to these are processed in accordance with KVQA ASSESSMENT PRIVATE LIMITED.</p>
            <p>Provisions and the content stated in Confirmation of certification scope (C600-FormJ) provided by auditor during audit will be final decision.</p>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 5: Granting issuance of certificate</v-card-title>
          <v-card-text>
            <p>Certification body reviews the result of corrective actions taken and submitted by the applicant and approves granting of certification. The certificate can only be issued with certification committee's review after all corrective actions are reviewed as per certification system. </p>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 6: Use of certification mark</v-card-title>
          <v-card-text>
            <p>On receipt of the certificate, the applicant shall comply with "Guide for use of certification mark and logo" and the Actions for misusing certification mark described there in, which are provided with certificate by the certification body.</p>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 7: Surveillance audit</v-card-title>
          <v-card-text>
            <v-list>
              <v-list-item>
                <v-list-item-content>
                  <p><strong>1. </strong>Surveillance audit for the applicant shall be carried out semi-annually or annually as per the quotation after the date of certification, pursuant to current Surveillance audit procedure of the certification body.</p>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <p><strong>2. </strong>Surveillance audit for the applicant shall be carried out semi-annually or annually as per the quotation after the date of certification, pursuant to current Surveillance audit procedure of the certification body.</p>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 8: Notification of changes in certification scope & changing audit</v-card-title>
          <v-card-text>
            <p>The applicant (certified organization) shall implement its duties and notify the certification body of the following changes as soon as they occur. After review the changes the certification body, if necessary, can perform the special surveillance audit or changing audit.</p>
            <v-list>
              <v-list-item>
                <v-list-item-content>
                  <p><strong>1. </strong>	Changes of company name or president.</p>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <p><strong>2. </strong>Changes of their significant organization structure, expansion or movement of premises during certification.</p>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <p><strong>3. </strong>Obtaining of serious complaints from an applicant/certified organization or interested party.</p>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <p><strong>4. </strong>Environmental accident occurred or violation of relevant laws, for EMS.</p>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <p><strong>5. </strong>	Changes occurred from expansion or reduction of certification scope (Standard, products applied for certification).</p>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 9: Renewal audit</v-card-title>
          <v-card-text>
            <p>Certification body shall carry out renewal audit against an applicant’s QMS/EMS and renew its certificate, within 3 years after certification, to continually ensure that its QMS/EMS is maintained and remains effective.</p>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 10: Liability of certification body</v-card-title>
          <v-card-text>
            <p>When the certified body is no longer maintained because certification activities are stopped and its accreditation is suspended and withdrawer, the certification shall, in consultation with the applicant, recommend another certification body or cooperation body for the applicant to maintain or re-register its certification. Such a case, according to mutual agreement, the certification body shall cover expense raised from it.</p>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 11: Suspension of certification</v-card-title>
          <v-card-text>
            <p>The certification body shall suspend certification when:</p>
            <v-list>
              <v-list-item>
                <p><strong>1. </strong>Surveillance audit was not performed within 1 month after the certified organization received notification letter& it’s surveillance audit was not carried out within specified time frame.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>2. </strong>With result of audit, it is shown that resources and organizational entity to satisfy with requirements of standard applied do not exist or certification system is no longer operated.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>3. </strong>There is absence of reliability on certification system because of claims raised by interested party and social conflicts, Certified organization has not taken any action for changes of certification system and certification requirements.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>4. </strong>The major non-conformity is re-occurred in follow-up audit which was performed to check corrective action taken for major non-conformity indicated on-site verification audit.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>5. </strong>Corrective action for misuse of certification mark has not been taken within 1 month after it is requested.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>6. </strong>Certification fee is not paid.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>7. </strong>The certified organization does not observe its duties defined in certification contract.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>8. </strong>The certified organization uses the certificate beyond its scope applied.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>9. </strong>All information and documents obtained in the course of certification activities turn out to be false.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>10. </strong>The problem with registering certification has been occurred because changes as described in article 8 have not been notified to certification body.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>11. </strong>The certified organization violets its agreement with KVQA ASSESSMENT PRIVATE LIMITED.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>12. </strong>Corrective action for minor nonconformity has not been verified within 30 days.</p>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 12: Withdrawal/Termination of certification</v-card-title>
          <v-card-text>
            <v-list>
              <v-list-item>
                <p><strong>1. </strong>Certification body withdraws certification and reports the fact on the publication in the event that the applicant does not comply with that,</p>
              </v-list-item>
              <v-list-item>
                <p><strong>2. </strong>Corrective action has not been taken within 3 months, despite suspension of certification as mentioned in Article 11; the certified applicant officially returns the certificate to certification body; </p>
              </v-list-item>
              <v-list-item>
                <p><strong>3. </strong>Production, activities or services of certified products have been suspended;</p>
              </v-list-item>
              <v-list-item>
                <p><strong>4. </strong>The certified organization is no longer identified because of its dismantlement or communication disconnecting etc.;</p>
              </v-list-item>
              <v-list-item>
                <p><strong>5. </strong>Certification has been suspended more than three times during its validation;</p>
              </v-list-item>
              <v-list-item>
                <p><strong>6. </strong>The applicant does not return the certificate to the certification body within 1 month after request by the certification body.</p>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 13: Appeals, complaints and disputes</v-card-title>
          <v-card-text>
            <p>When the applicant has appeals, complaints and disputes regarding certification audit and related to certification, the applicants shall notify it to the certification body in written statement. Such appeals, complaints and disputes brought to the certification body shall be subject to the procedures of the certification body and the result thereof shall be notified to the applicant in writing.</p>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 14: Confidentiality</v-card-title>
          <v-card-text>
            <p>The certification body shall not disclose information about the applicant’s organization or a particular product to a third party without the written consent of the applicant, except where accreditation body requires. When the certification discloses information to a third party, as permitted by the law, the certification body shall inform it to the applicant. However, this is not applied for,</p>
            <v-list>
              <v-list-item>
                <p><strong>- </strong>Information that certification body already has before the applicant provided;</p>
              </v-list-item>
              <v-list-item>
                <p><strong>- </strong>Information legally well-known or expected to be well known to public;</p>
              </v-list-item>
              <v-list-item>
                <p><strong>- </strong>Information legally obtained from where it is not related to the applicant;</p>
              </v-list-item>
              <v-list-item>
                <p><strong>- </strong>Information required by Accreditation body for its evaluation of certification body. Information about the client from sources other than the client (e.g. complainant, regulators), shall be treated as confidential, consistent with the KVQA ASSESSMENT PRIVATE LIMITED Certification body’s policy.</p>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 15: Changes in the certification requirements</v-card-title>
          <v-card-text>
            <p>When certification requirements by certification body have been changed, the following shall be processed within specified period:</p>
            <v-list>
              <v-list-item>
                <p><strong>1. </strong>The certification body shall give due notice of any change and its effective date to the applicant 1 Month in advance.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>2. </strong>The applicant shall submit documented plan of subsequent action in details or its result according to certification requirements changed.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>3. </strong>The certification body. in surveillance audit, shall verify the applicant’s implementation in Compliance with requirements changed, within 12 months</p>
              </v-list-item>
            </v-list>
        </v-card-text>
        </v-card>
        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 16: Certification Fee</v-card-title>
          <v-card-text>
            <v-list>
              <v-list-item>
                <p><strong>- </strong>Certification fee (Registration, Preaudit, Document audit, Cert Audit, Reaudit, and Registration) is specified in Quotation.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>- </strong>Surveillance audit fee is charged as per audit fee in quotation when it is carried out.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>- </strong>When major nonconformity is found during audit or certification, on-site follow-up audit will be required and the expenses will be charged as per audit fee rate on the time of visit.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>- </strong>Travel expense, accommodation expenses of certification body, raised from audit, shall be charged to the applicant.</p>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 17: Payment</v-card-title>
          <v-card-text>
            <v-list>
              <v-list-item>
                <p><strong>1. </strong>When concluding a contract, the applicant shall pay allfees as per quotation, when submitting forms.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>2. </strong>Audit fee (document audit fee, pre-audit fee, on-site audit fee, follow-up audit fee, and surveillance audit fee) shall be paid on receipt of Invoice. All invoices shall be paid within 7 days from its receipt of the invoice.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>3. </strong>Traveling expenses are charged with audit fee.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>4. </strong>All fees with all taxes have to be borne by the client.</p>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 18: Irresistible force</v-card-title>
          <v-card-text>
            <p>Any liability for indirect and consequential damage, including war, natural disaster, an infectious diseases and closedown of factory etc which are beyond control, is hereby excluded.</p>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 19: Contract interpretation and disputes settlement</v-card-title>
          <v-card-text>
            <p>Every dispute or question, which may arise between the parties of this contract, shall be amicably settled. If the lawsuit occurs, the place of jurisdiction for the claims shall be in Delhi.</p>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 20: Reliability, faithfulness and mutual co-operation</v-card-title>
          <v-card-text>
            <v-list>
              <v-list-item>
                <p><strong>1. </strong>Both applicant and certification body shall comply with all the articles stated in contract upon mutual trust and endeavor to maximize the achievement of goals. Certification body impartially implements its certification services and the applicant gives best assistance to certification body for its effective implementation of certification services.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>2. </strong>The applicant shall comply with all laws   related to QMS/EMS certification and give assistance for special surveillance audit required by Accreditation body, if any.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>3. </strong>The applicant should allow trainee to participate in audit.</p>
              </v-list-item>
              <v-list-item>
                <p><strong>4. </strong>When certified applicant/organization is transferred to another certification body, it, as well as the reason thereof, shall be informed to certification body.</p>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 21: Period of contract</v-card-title>
          <v-card-text>
            <p>This agreement shall come into force on signature by the two parties and shall definitely run for at least a period of three years. It shall be extended by a further three years in each case on placement of an order for renewal by applicant.</p>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-divider></v-divider>

        <v-card class="mb-3" outlined>
          <v-card-title class="text-h6 font-weight-bold">Article 22: Retention of contract</v-card-title>
          <v-card-text>
            <p>Both parties ensure to comply with all articles above stated and for its evidence, contract (duplicate) duly signed by representative of both parties shall be kept at both sides.</p>
          </v-card-text>
        </v-card>

        <v-divider></v-divider>

        <v-table>
          <v-row>
            <v-col cols="12" md="6">
              <v-row>
                <v-col cols="12" md="6">
                  <p>Name: </p>
                </v-col>
                <v-col cols="12" md="6">
                  <v-text-field label="Company Name" v-model="companyname" required></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" md="6">
                  <v-text-field label="Signature" v-model="companysignature" required></v-text-field>
                </v-col>
                <v-col cols="12" md="6">
                  <v-text-field label="Company Seal" v-model="companyseal" required></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" md="12">
                  <v-text-field label="For" v-model="companydetails" required></v-text-field>
                </v-col>
              </v-row>
            </v-col>
            <v-col cols="12" md="6">
              <v-row>
                <v-col cols="12" md="6">
                  <p>Lav Kaushik</p>
                </v-col>
                <v-col cols="12" md="6">
                  <v-text-field label="KVQA Name" v-model="kvqaname" required></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" md="6">
                  <p>KVQA Signature</p>
                </v-col>
                <v-col cols="12" md="6">
                  <v-text-field label="KVQA Seal" v-model="kvqaseal" required></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" md="12">
                  <p>(For and behalf of KVQA ASSESSMENT PRIVATE LIMITED.)New Delhi</p>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-table>
      </v-card>
    </v-container>
  </template>
  
  <script>
  export default {
    name: "CertificationContract",

    data() {
      return {
        companyname: "",
        kvqaname: "",
        companysignature: "",
        companyseal: "",
        kvqaseal: "",
        companydetails: "",
      }
    }
  };
  </script>
  
  <style scoped>
  p {
    font-size: 16px;
    line-height: 1.5;
  }
  </style>
  