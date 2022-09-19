// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// IMPORTS
import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC1155/utils/ERC1155Holder.sol";

contract NFT is ERC1155, ERC1155Holder{

    // tokenid should be autoincremented everytime nft is created ✔️
    // override the uri() function to return the custom metadatauri of nfts ✔️
    // booth owner needs data regarding nfts he owns. So mynft function must return all the nfts owned by him ✔️
    // implement buy logic ✔️

    // GLOBALS
    using Counters for Counters.Counter;
    Counters.Counter private _tokenId;
    struct NFTlist{
        uint256 tokenId;
        uint256 price;
        string name;
        string metadataURI;
        address owner;
        string imageuri;
    }
    mapping(uint256 => string)  tokenIdToMetadatURI;
    mapping(uint256 => NFTlist)  tokenIdToNFTdata;
    mapping(address => uint256) public owings;
    uint256 listingPrice = 1000000 gwei;
    

    // CONSTRUCTOR
    constructor() ERC1155("RANDOMLINK"){
    }

    // OVERRIDE FUNCTIONS
    // overriding supportsInterface (mandatory for contracts to receive nfts)
     function supportsInterface(bytes4 interfaceId) public view virtual override(ERC1155, ERC1155Receiver) returns (bool) {
        return super.supportsInterface(interfaceId);
    }

    // overriding uri function to return custom metadataURI
    function uri(uint256 tokenId) public view override returns(string memory){
        return tokenIdToMetadatURI[tokenId];
    }
    
    // FUNCTIONS
    // mint nfts
    function mintNFT(string memory metadataURI, string memory name, uint256 price, string memory imageURI) payable external {
        require(msg.value == listingPrice, "a small fee for listing is required");
        require(price >= 10000000 gwei, "minimum price must be 0.01 MATIC");

        // increment tokenId
        _tokenId.increment();

        // mint the nft to the function caller
        _mint(address(this), _tokenId.current(), 1, "");

        // set the metadataURI
        setUri(_tokenId.current(), metadataURI);

        // add minted nft data to nftlist
        addNFTtoNFTlist(_tokenId.current(), name, metadataURI, price, msg.sender, imageURI);
    }   

    // get nft data
    function getNFTdata(uint256 tokenId) public view returns(NFTlist memory){
        return tokenIdToNFTdata[tokenId];
    }

    // function to store metadata uri
    function setUri(uint256 tokenId, string memory metadataURI) internal{
        tokenIdToMetadatURI[tokenId] = metadataURI;
    }

    // add nft metadata to nftlist
    function addNFTtoNFTlist(uint256 tokenId, string memory name, string memory metadataURI, uint256 price, address owner, string memory imageURI) internal {
        tokenIdToNFTdata[tokenId] = NFTlist(tokenId, price, name, metadataURI, owner, imageURI);
    }

    // get all nfts owned by booth owner
    function mynft(address owner) public view returns(NFTlist[] memory){
        // calculate the array length required
        uint256 currentIndex = 0;
        for(uint256 id = 0; id <= _tokenId.current(); id++){
            NFTlist memory data = tokenIdToNFTdata[id];
            if (data.owner == owner){
                currentIndex++;
            }
        }
        // return the array
        NFTlist[] memory listval = new NFTlist[](currentIndex);
        currentIndex = 0;
        for(uint256 id = 0; id <= _tokenId.current(); id++){
            NFTlist memory data = tokenIdToNFTdata[id];
            if (data.owner == owner){
                listval[currentIndex] = data;
                currentIndex++;
            }
        }
        return listval;
    }

    // buy function
    function buy(uint256 tokenId) public payable {
        NFTlist memory data = tokenIdToNFTdata[tokenId];
        uint256 price = data.price;
        require(msg.value == price, "send the accurate price");
        owings[data.owner] += price;
        data.owner = msg.sender;
        tokenIdToNFTdata[tokenId] = data;
    }

    // withdraw funds
    function withdraw() external {
        require(owings[msg.sender] > 0, "can't withdraw funds.");
        require(payable(msg.sender).send(owings[msg.sender]), "error occurred");
        owings[msg.sender] = 0;
    }
}
