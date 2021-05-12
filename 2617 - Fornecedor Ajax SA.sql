select products.name, providers.name
from products
inner join providers on (providers.id = products.id_providers) and providers.name = 'Ajax SA';
