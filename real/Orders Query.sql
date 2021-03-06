SELECT NAME, PRICE

FROM ORDERS, CUSTOMERS

WHERE CUSTOMERS.ORDER_ID = ORDERS.ID

AND ORDERS.PRICE =

(SELECT MAX(PRICE) FROM ORDERS

WHERE ORDER_DATE BETWEEN

(SELECT MIN(ORDER_DATE) FROM ORDERS) AND

(SELECT DATE_ADD(MIN(ORDER_DATE), INTERVAL 10 year) FROM ORDERS))

ORDER BY ORDERS.PRICE DESC LIMIT 1;