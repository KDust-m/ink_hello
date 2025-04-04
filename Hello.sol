pragma solidity 0.8.28;

contract Hello {
    event HELLO(address indexed user, address indexed recipient);

    function hello() external {
        emit HELLO(msg.sender, address(0));
    }
}
