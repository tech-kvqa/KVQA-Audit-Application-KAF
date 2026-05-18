import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Home.vue'
import AdminLogin from '../views/AdminLogin.vue'
import SalesLogin from '../views/SalesLogin.vue'
import ConsultantLogin from '../views/ConsultantLogin.vue'
import AdminDashboard from '../views/AdminDashboard.vue'
import AdminUsers from '../components/admin/users.vue'
import AdminConsultants from '../components/admin/consultants.vue'
import AdminSales from '../components/admin/sales.vue'
import AdminApplication from '../components/admin/application.vue'
import ConsultantDashboard from '../views/ConsultantDashboard.vue'
import ConsultantApplication from '../components/consultants/application.vue'
import ConsultantApplicationForm from '../components/consultants/applicationform.vue'
import ConsultantQuestionnaire from '../components/consultants/questionnaire.vue'
import ConsultantQuestionnaireEMS from '../components/consultants/ems.vue'
import ConsultantQuestionnaireQMS from '../components/consultants/qms.vue'
import SalesDashboard from '../components/sales/SalesDashboard.vue'
import SalesApplication from '../components/sales/Application.vue'
import SalesApplicationForm from '../components/sales/SalesApplicationForm.vue'
import Upload from '../components/sales/Upload.vue'
import SendQuotation from '../components/sales/SendQuotation.vue'
import ViewExcel from '../components/sales/ViewExcel.vue'
import Kaf2 from '../components/sales/Kaf2.vue'
import Kaf3 from '../components/sales/Kaf3.vue'
import Kaf4 from '../components/sales/Kaf4.vue'
import DetailsPage from '@/views/DetailsPage.vue'
import DecisionMakerLogin from '@/views/DecisionMakerLogin.vue'
import DecisionMakerDashboard from '@/views/DecisionMakerDashboard.vue'
import DecisionMakerDetailsPage from '@/views/DecisionMakerDetailsPage.vue'

const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/admin/login', name: 'AdminLogin', component: AdminLogin },
  { path: '/consultant/login', name: 'ConsultantLogin', component: ConsultantLogin },
  { path: '/sales/login', name: "SalesLogin", component: SalesLogin },
  { path: '/decision-maker/login', name: "DecisionMakerLogin", component: DecisionMakerLogin },
  { path: '/admin/dashboard', name: 'AdminDashboard', component: AdminDashboard },
  { path: '/admin/users', name: 'AdminUsers', component: AdminUsers },
  { path: '/admin/consultants', name: 'AdminConsultants', component: AdminConsultants },
  { path: '/admin/sales', name: 'AdminSales', component: AdminSales },
  { path: '/admin/application', name: 'AdminApplication', component: AdminApplication },
  { path: '/consultant/dashboard', name: 'ConsultantDashboard', component: ConsultantDashboard },
  { path: '/consultant/application', name: 'ConsultantApplication', component: ConsultantApplication },
  { path: '/consultant/applicationform', name: 'ConsultantApplicationForm', component: ConsultantApplicationForm },
  { path: '/consultant/questionnaire', name: 'ConsultantQuestionnaire', component: ConsultantQuestionnaire },
  { path: '/consultant/questionnaire/ems', name: 'ConsultantQuestionnaireEMS', component: ConsultantQuestionnaireEMS },
  { path: '/consultant/questionnaire/qms', name: 'ConsultantQuestionnaireQMS', component: ConsultantQuestionnaireQMS },
  { path: '/sales/dashboard', name: 'SalesDashboard', component: SalesDashboard },
  { path: '/sales/application', name: 'SalesApplication', component: SalesApplication },
  { path: '/sales/applicationform', name: 'SalesApplicationForm', component: SalesApplicationForm },
  { path: '/upload/:token', name: 'Upload', component: Upload, props: true },
  { path: '/sales/send-quotation/:companyId',name: 'SendQuotation', component: SendQuotation, props: true },
  { path: '/sales/view-excel/:companyName/:questionnaireType', name: 'ViewExcel', component: ViewExcel, props: true },
  { path: '/sales/kaf2', name: Kaf2, component: Kaf2 },
  { path: '/sales/kaf3', name: Kaf3, component: Kaf3 },
  { path: '/sales/kaf4', name: Kaf4, component: Kaf4 },
  { path: '/sales/details/:companyId', name: 'Details Page', component: DetailsPage,  props:true},
  { path: '/decision-maker/dashboard', name: 'DecisionMakerDashboard', component: DecisionMakerDashboard },
  { 
    path: '/decision-maker/details/:companyId',
    name: 'DecisionMakerDetailsPage',
    component: DecisionMakerDetailsPage,
    props: true
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
