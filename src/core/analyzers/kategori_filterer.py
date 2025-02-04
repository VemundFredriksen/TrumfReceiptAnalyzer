from typing import List
from models.kategori_aggregate import KategoriAggregate
from models.vare_aggregate import VareAggregate
from models.kategori import Kategori


class KategoriFiltrer:
    
    def filtrer(self, kategori: Kategori, vare_aggregates: List[VareAggregate]) -> KategoriAggregate:
        aggregates = []
        for varekategori in kategori.kategorier:
            included_varer = list(filter(lambda v: v.varenavn in varekategori.inkluderte_varer, vare_aggregates)) 
            totalsum = sum(map(lambda k: k.total_belop,  included_varer))
            antall = sum(map(lambda k: k.total_antall, included_varer))
            
            aggregates.append(KategoriAggregate(varekategori.navn, totalsum, antall))
            if kategori.exclusive:
                vare_aggregates = list(filter(lambda v: v.varenavn not in varekategori.inkluderte_varer, vare_aggregates))
            
        return aggregates