# OSPF Configuration

## 1. Khởi tạo OSPF

- Tạo OSPF Process  
  * router ospf <process-id>

- Đặt Router ID  
  * router-id <A.B.C.D>

- Quảng bá mạng  
  * network <network> <wildcard-mask> area <area-id>

- Khởi động lại OSPF Process  
  * clear ip ospf process

---

## 2. OSPF trên Interface

- Kích hoạt OSPF trên interface  
  *  interface <interface>  
     *  ip ospf <process-id> area <area-id>

- Đổi Network Type  
  *  interface <interface>  
     *  ip ospf network ?  
        *** broadcast  
        *** non-broadcast  
        *** point-to-point  
        *** point-to-multipoint  

---

## 3. Passive Interface

- Chặn gửi Hello trên tất cả interface  
  * ** router ospf <process-id>  
    ** passive-interface default

- Cho phép interface gửi Hello  
  * ** router ospf <process-id>  
    ** no passive-interface <interface>

---

## 4. Hello / Dead Timer

- Đổi Hello Interval  
  * ** interface <interface>  
    ** ip ospf hello-interval <seconds>

- Đổi Dead Interval  
  * ** interface <interface>  
    ** ip ospf dead-interval <seconds>

---

## 5. Authentication

- Plain Text Authentication  
  * ** interface <interface>  
    ** ip ospf authentication  
    ** ip ospf authentication-key <password>

- MD5 Authentication  
  * ** interface <interface>  
    ** ip ospf authentication message-digest  
    ** ip ospf message-digest-key <key-id> md5 <password>

---

## 6. Cost

- Chỉnh OSPF Cost  
  * ** interface <interface>  
    ** ip ospf cost <cost>

- Chỉnh Reference Bandwidth  
  * ** router ospf <process-id>  
    ** auto-cost reference-bandwidth <Mbps>

---

## 7. MTU

- Đổi MTU  
  * ** interface <interface>  
    ** ip mtu <bytes>

- Bỏ kiểm tra MTU  
  * ** interface <interface>  
    ** ip ospf mtu-ignore

---

## 8. Neighbor (NBMA)

- Khai báo Neighbor thủ công  
  * ** router ospf <process-id>  
    ** neighbor <ip-address>

---

# RIP Configuration

## 1. Khởi tạo RIP

- Khởi tạo RIP  
  * ** router rip

- Chọn Version  
  * ** version 1  
  * ** version 2

- Quảng bá Network  
  * ** network <network>

- Tắt Auto Summary  
  * ** no auto-summary

---

## 2. Passive Interface

- Chặn gửi RIP Update  
  * ** passive-interface <interface>

- Bỏ Passive  
  * ** no passive-interface <interface>

---

## 3. Default Route

- Tạo Default Route  
  * ** ip route 0.0.0.0 0.0.0.0 <next-hop>

- Quảng bá Default Route  
  * ** default-information originate

---

## 4. Timer

- Thay đổi Timer  
  * ** timers basic <update> <invalid> <holddown> <flush>

---

## 5. Authentication (RIPv2)

- Plain Text  
  * ** interface <interface>  
    ** ip rip authentication mode text  
    ** ip rip authentication key-chain <name>

- MD5  
  * ** interface <interface>  
    ** ip rip authentication mode md5  
    ** ip rip authentication key-chain <name>

- Tạo Key Chain  
  * ** key chain <name>  
    ** key <id>  
      *** key-string <password>

---

## 6. Verify

- Kiểm tra RIP  
  * ** show ip protocols

- Kiểm tra Routing Table  
  * ** show ip route

- Kiểm tra RIP Database  
  * ** show ip rip database

- Debug RIP  
  * ** debug ip rip