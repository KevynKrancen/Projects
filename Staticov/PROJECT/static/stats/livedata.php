<?php
header('Content-type: application/json');

// Please Update 
$purchase_code = 'your_purchase_code';


// DO NOT REMOVE OR EDIT BELLOW
////////////////////////////////////////////////////
function fetch_from_live($url){
	global $softnio_apikey;
    $ch = curl_init();
    $headers = array(
        'Accept: application/json',
        'Content-Type: application/json',
        'nio-apikey: NIO35223TH32',
    );
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_HEADER, 0);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_TIMEOUT, 300);
    $response = curl_exec($ch);
    return $response;
}

function get_live_data(){
	global $purchase_code; $host = base64_encode(str_replace('www.', '', $_SERVER["SERVER_NAME"]));
	$api_uri = 'https://covid.softnio.com/api/countries/full';
	$pco_uri = ($purchase_code) ? '?code='.$purchase_code : '';
	$req_uri = ($host) ? '&uri='.$host : '';
	return fetch_from_live($api_uri.$pco_uri.$req_uri);
}

function get_covid_data(){
	$local_stats  = __DIR__.'/stats.json';
	$updated  = __DIR__.'/updated.json';

	$update_live = true;
	$update_time = 900;
	$time_current = $last_update = time();

	if(file_exists($updated)){
	    $last_update = file_get_contents($updated);
	    if (($time_current - $last_update) <= $update_time) {
		    $update_live = false;
		}
	} else {
		file_put_contents($updated, $last_update);
	}

	try {
		if($update_live===true) {
	    	$live_data = get_live_data();
		    if(!empty($live_data)){
		        file_put_contents($local_stats, $live_data);
		        file_put_contents($updated, $time_current);
		    } else {
		        if(file_exists($local_stats)){
		            $live_data = file_get_contents($local_stats);
		        }
		    }
		} else {
			if(file_exists($local_stats)){
	            $live_data = file_get_contents($local_stats);
	        } else {
	        	$live_data = get_live_data();
	        	if(!empty($live_data)){
			        file_put_contents($local_stats, $live_data);
			        file_put_contents($updated, $time_current);
			    }
	        }
		}

	} catch (\Exception $e) {}

	if(!empty($live_data)) {
		return json_decode($live_data, true);
	} else {
		return false;
	}
}

function get_data($code=''){
	$stats = get_covid_data();
	$output = [];

	if(strtolower($code)=='all' && !empty($stats)) {
		return $stats;
	}

	if(!empty($stats)) {
		$global = (isset($stats['world'])) ? $stats['world'] : false;
		if(empty($code) && !empty($global)) {
			$output = $global;
		} else {
			$country = (isset($stats[strtolower($code)])) ? $stats[strtolower($code)] : false;
			if(!empty($country)) {
				$output = $country;
			}
		}
	}

	if($output && isset($output['update'])) {
		$output['update'] = date('M d, Y, h:i A e', $output['update']);
	}

	return $output;
}

$code = $_REQUEST['code'];
$error = ['status' => 'error', 'response' => 'Requested data not available.'];
if (empty($code)) {
	$output = json_encode(['status' => 'error', 'response' => 'Unable to process request.']);
	echo $output;
} else {
	if($code=='countries') {
		$data = get_data('all');
		if(!empty($data)) {
			$output = json_encode(['status' => 'success', 'response' => $data]);
		} else {
			$output = json_encode($error);
		}
	} else {
		$data = get_data($code);
		if(!empty($data)) {
			$output = json_encode(['status' => 'success', 'response' => $data]);
		} else {
			$output = json_encode($error);
		}
	}
	echo $output;
}