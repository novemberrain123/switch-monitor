# switch-monitor
## Task 1:
1) Empty table is created in MySQL server
2) Empty table is filled with:

```
load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/data_terminals.csv'
into table pingstatus fields terminated by ','
lines terminated by '\n'
ignore 1 rows (switch_label, term_1, term_2, term_3, term_4, term_5, @var1)
set ts = from_unixtime(@var1);
```

SS of database:

![image](https://user-images.githubusercontent.com/57749508/206892220-8fbbf32b-d980-4ba3-b324-5a1611b19c76.png)

## Task 2:
1) Create django project.
2) Migrate existing database into django models.
3) Create other features.

### Update switch status feature

Easier way to do this is in MySQL database whenever new data is added but to showcase ajax POST this method is used.

SS of homepage:

![image](https://user-images.githubusercontent.com/57749508/206892143-1646deb3-26c3-4ba0-adfc-1f73fbafad99.png)

Alert given after database updated:

![image](https://user-images.githubusercontent.com/57749508/206892182-84690f9d-1972-4510-9907-3e5bdaa8a10f.png)

### Ping availability charts

Filtered by date and timerange (0000-1159 or 1200-2359), separated into n charts for each switch available. Code written in a way that allows for additional switches (not tested).

SS of feature:

![image](https://user-images.githubusercontent.com/57749508/206892398-a2210675-7bde-4799-9555-ac8f9dcd95a8.png)

### Alert report page

SS of feature:

![image](https://user-images.githubusercontent.com/57749508/206892414-8ab25cbd-366c-422e-91ec-c97a945fd3fe.png)

