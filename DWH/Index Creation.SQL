CREATE INDEX Tran_branch on Transactions_Fact(BRANCH_ID);
CREATE INDEX Tran_cust on TraAPPROVEDnsactions_Fact(CUSTOMER_ID);
CREATE INDEX Tran_service on Transactions_Fact(SERVICE_ID);
CREATE INDEX Tran_date on Transactions_Fact(DATE_ID);

CREATE INDEX MC_cust on marketing_campaign_Fact(CUSTOMER_ID);
CREATE INDEX MC_service on marketing_campaign_Fact(SERVICE_ID);
CREATE INDEX MC_date on marketing_campaign_Fact(DATE_ID);

CREATE INDEX CS_cust on customer_services_Fact(CUSTOMER_ID);
CREATE INDEX CS_service on customer_services_Fact(SERVICE_ID);
CREATE INDEX CS_date on customer_services_Fact(DATE_ID);
CREATE INDEX CS_member on customer_services_Fact(MEMBER_ID);
CREATE INDEX CS_branch on customer_services_Fact(BRANCH_ID);