from Scaffold_Code import block, wallet , config ,chain

class Node: #creation of bootstap node
	def __init__(self):
		#self.NBC=100
		##set
		self.current_block  #san transaction pool me transactions<=maximum
		#self.chain
		#self.current_id_count
		self.wallet = create_wallet()
		self.transaction_pool
		#slef.ring[]   #here we store information for every node, as its id, its address (ip:port) its public key and its balance 




	#def create_new_block(previousHash): #an einai to proto 
				
		

		
	def create_wallet():
		##create a wallet for this node, with a public key and a private key
		return Wallet()

	def register_node_to_ring():
		#add this node to the ring, only the bootstrap node can add a node to the ring after checking his wallet and ip:port address
		#bottstrap node informs all other nodes and gives the request node an id and 100 NBCs


	def create_transaction(sender, receiver, signature):
		#remember to broadcast it


	def broadcast_transaction():


	def verify_signature(wallet_address, message, signature):
		pubkey = RSA.importKey(binascii.unhexlify(wallet_address))
    	verifier = PKCS1_v1_5.new(pubkey)
        h = SHA.new(message.encode('utf8'))
    return verifier.verify(h, binascii.unhexlify(signature))


    


	def validate_transaction(transaction):
		#when receiving a transaction, first validate with the signature
		#second, check if UTXOs are enough to make the transaction
		#if validation is OK, add transaction to current block
		if not isinstance(transaction, GenesisTransaction): {

		# Verify input transactions
		for tx in transaction.inputs:
        	if not validate_transaction(tx.transaction): 
            	logging.error("Invalid parent transaction")
            	return False
		}

	def add_transaction_to_block(current_block , transaction , previousHash): 
		#if
		#if enough transactions  mine
		if (len(current_block) == max_transactions):
			new_block = Block(previousHash , current_block)
			mine_block(current_block)
			broadcast_block(current_block)
		else:
			current_block.append(transaction)



	def mine_block( block ):
		 last_block = self.chain[-1]
		## message= kati to_dict 
		 nonce = self.valid_proof(message)
		 block.add_nonce(nonce)
		 self.broadcast_block()
		 chain.add_block_to_mychain(block)



	def broadcast_block():


	

	def valid_proof(message , prefix=DIFFICULTY):
		i = 0
    	prefix = '1' * difficulty
    	while True:
			nonce = str(i)
			digest = dumb_hash(message + nonce)
			if digest.startswith(prefix):
				return nonce
			i += 1



	#concencus functions

	def valid_chain(self, chain):
		#check for the longer chain accroose all nodes ????
		#check if a bockchain is valid


	def resolve_conflicts(self):
		#resolve correct chain



