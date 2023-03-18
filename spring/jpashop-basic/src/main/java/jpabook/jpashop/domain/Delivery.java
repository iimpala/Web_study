package jpabook.jpashop.domain;

import javax.persistence.*;

import static javax.persistence.FetchType.LAZY;

@Entity
public class Delivery extends BaseEntity{

    @Id @GeneratedValue
    private Long id;

    @OneToOne(mappedBy = "delivery", fetch = LAZY)
    private Order order;

    @Embedded
    private Address address;

    private DeliveryStatus status;
}
