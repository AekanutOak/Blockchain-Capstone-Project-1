//SPDX-License-Identifier: MITchange
pragma solidity 0.8.19; //Use complier version 0.8.19

contract Product{
    struct product_record{
        string name;
        string origin;
        string manufacturer;
        string product_info;
        string current_owner;
        address current_owner_address;
        uint256 timestamp;
    }

    string[] list_product;

    mapping(string => product_record[]) product_track_table;

    function get_product_record(
        string memory product_ID
    ) public view returns (product_record[] memory){
        return product_track_table[product_ID];
    }

    function get_last_product_record(
        string memory product_ID
    ) public view returns (product_record memory){
        product_record[] memory record = product_track_table[product_ID];
        return record[record.length - 1];
    }

    function get_product_list() public view returns (string[] memory){
        return list_product;
    }

    function add_new_product(
        string memory product_ID,
        string memory name,
        string memory origin,
        string memory manufacturer,
        string memory product_info,
        string memory current_owner,
        address current_owner_address
    ) public returns(string memory){
        require(
            product_track_table[product_ID].length == 0,
            "Duplicated product number."
        );

        product_track_table[product_ID].push(
            product_record(
                name,
                origin,
                manufacturer,
                product_info,
                current_owner,
                current_owner_address,
                block.timestamp
            )
        );

        list_product.push(product_ID);
        return product_ID;
    }
}