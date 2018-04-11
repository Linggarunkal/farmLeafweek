function enableBankAccount(){
	if(document.getElementById('modify').checked == true){
		document.getElementById('behalfAccount').disabled = false;
		document.getElementById('bankNumber').disabled = false;
		document.getElementById('bankBranch').disabled = false;
		document.getElementById('save').disabled = false;
		document.getElementById('submit').disabled = true;
	}
	else{
		document.getElementById('behalfAccount').disabled = true;
		document.getElementById('bankNumber').disabled = true;
		document.getElementById('bankBranch').disabled = true;
		document.getElementById('save').disabled = true;
		document.getElementById('submit').disabled = false;
	}

}