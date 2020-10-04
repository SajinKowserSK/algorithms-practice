/*
Enter your query below.
Please append a semicolon ";" at the end of the query
*/

SELECT COALESCE(c.customer_name, "N/A"), COALESCE(p.product_name, "N/A"), COALESCE(ii.quantity, 0) 

FROM customer c 

left join invoice i on c.id = i.customer_id 

join invoice_item ii on i.id = ii.invoice_id 

right join product p on ii.product_id = p.id 

order by c.id, p.id, ii.id;