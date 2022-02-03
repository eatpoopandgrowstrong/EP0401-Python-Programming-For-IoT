package com.example.iot_storyboarding

import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.graphics.BitmapFactory
import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.core.app.ActivityCompat
import androidx.core.app.NotificationCompat
import androidx.core.app.NotificationManagerCompat
import com.android.volley.Request
import com.android.volley.Response
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import com.example.iot_storyboarding.databinding.ActivityMainBinding
import com.google.android.gms.location.FusedLocationProviderClient
import com.google.android.gms.location.LocationServices
import kotlin.math.cos

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    //var homeLatitude by Delegates.notNull<Double>()
    //var homeLongitude by Delegates.notNull<Double>()

    //var currentLatitude by Delegates.notNull<Double>()
    //var currentLongitude by Delegates.notNull<Double>()

    lateinit var fusedLocationProviderClient: FusedLocationProviderClient
    /*
    var currentLatitude = ""
    var currentLongitude = ""

     */
    private val CHANNEL_ID = "channel_id_notification"
    private val notificationId = 101

    private var stateLED1 = 0
    private var stateLED2 = 0
    private var stateLED3 = 0
    private var stateLED4 = 0

    private var stateLED1checkBox = 0
    private var stateLED2checkBox = 0
    private var stateLED3checkBox = 0
    private var stateLED4checkBox = 0

    var distanceRadius = 0.3 // 0.3 km

    /*
    From a computing POV, the buttons and switches ("devices") should be generated via iteration
    instead of some hardcoding, but right now just get a mvp out

     */

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //binding.button.isEnabled = false
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        //set gps reset to be disabled by default
        binding.button.isEnabled = false

        createNotificationChannel()
        fusedLocationProviderClient = LocationServices.getFusedLocationProviderClient(this)
        fetchLocation()
        // 4 LIGHTING SWITCHES
        // Probably can be refactored, just do some concatenation with the LED number and state

        binding.switch1.setOnCheckedChangeListener { _, isChecked ->
            if (isChecked) {
                binding.textView1.text = "Debug: LED1 is ON"

                stateLED1 = 1
                postRequest()

            } else {
                // The toggle is disabled
                binding.textView1.text = "Debug: LED1 is OFF"

                //setLightsOff()
                stateLED1 = 0
                postRequest()

            }
        }

        binding.switch2.setOnCheckedChangeListener { _, isChecked ->
            if (isChecked) {
                binding.textView2.text = "Debug: LED2 is ON"

                stateLED2 = 1
                postRequest()

            } else {
                // The toggle is disabled
                binding.textView2.text = "Debug: LED2 is OFF"

                //setCurtainsToRetract()
                stateLED2 = 0
                postRequest()

            }
        }

        binding.switch3.setOnCheckedChangeListener { _, isChecked ->
            if (isChecked) {
                binding.textView3.text = "Debug: LED3 is ON"
                stateLED3 = 1
                postRequest()

            } else {
                // The toggle is disabled
                binding.textView3.text = "Debug: LED3 is OFF"
                stateLED3 = 0
                postRequest()

            }
        }

        binding.switch4.setOnCheckedChangeListener { _, isChecked ->
            if (isChecked) {
                binding.textView4.text = "Debug: LED4 is ON"
                stateLED4 = 1
                postRequest()

            } else {
                // The toggle is disabled
                binding.textView4.text = "Debug: LED4 is OFF"
                stateLED4 = 0
                postRequest()

            }
        }

        // just brute force this

        binding.SelectAllLEDCheckBox.setOnCheckedChangeListener { _, isChecked ->

            if (isChecked) {
                binding.LED1CheckBox.isChecked = true
                binding.LED2CheckBox.isChecked = true
                binding.LED3CheckBox.isChecked = true
                binding.LED4CheckBox.isChecked = true
            } else {

            }
        }

        binding.LED1CheckBox.setOnCheckedChangeListener { _, isChecked ->
            if (isChecked) {
                stateLED1checkBox = 1
            } else {
                stateLED1checkBox = 0
            }
            // TODO: REFACTOR STATES TO BOOL INSTEAD OF INT
            binding.SelectAllLEDCheckBox.isChecked =
                ((stateLED1checkBox == 1) and (stateLED2checkBox == 1)
                        and (stateLED3checkBox == 1) and (stateLED4checkBox == 1))
        }

        binding.LED2CheckBox.setOnCheckedChangeListener { _, isChecked ->
            if (isChecked) {
                stateLED2checkBox = 1
            } else {
                stateLED2checkBox = 0
            }
            binding.SelectAllLEDCheckBox.isChecked =
                ((stateLED1checkBox == 1) and (stateLED2checkBox == 1)
                        and (stateLED3checkBox == 1) and (stateLED4checkBox == 1))
        }

        binding.LED3CheckBox.setOnCheckedChangeListener { _, isChecked ->
            if (isChecked) {
                stateLED3checkBox = 1
            } else {
                stateLED3checkBox = 0
            }
            binding.SelectAllLEDCheckBox.isChecked =
                ((stateLED1checkBox == 1) and (stateLED2checkBox == 1)
                        and (stateLED3checkBox == 1) and (stateLED4checkBox == 1))
        }

        binding.LED4CheckBox.setOnCheckedChangeListener { _, isChecked ->
            if (isChecked) {
                stateLED4checkBox = 1
            } else {
                stateLED4checkBox = 0
            }
            binding.SelectAllLEDCheckBox.isChecked =
                ((stateLED1checkBox == 1) and (stateLED2checkBox == 1)
                        and (stateLED3checkBox == 1) and (stateLED4checkBox == 1))
        }

        binding.enableGPSSwitch.setOnCheckedChangeListener { _, isChecked ->

            binding.button.isEnabled = isChecked


        }

        binding.button.setOnClickListener {
            /*
            Idea of this is to test the reset of the switches to reflect the change in the lights'
            state when the device leaves the zone
            Cut and paste into GPS once done

            Might not need to use that super complex logic, just uncheck the state of the switch
            using setUnchecked

            Is the GPS feature enabled?
            -> Collected Via Toggle Switch
            Which devices would the user like to turn off?
            -> Collected Via Radio Buttons? Non-exclusive Radio Buttons
            -> Ideally 1 everything button to select everything instead of everything individually
                - Have maybe 10+ devices, select all 1 at a time LMAO
            Does there need to be logic to check whether the device is off?
            Can just brute force set all to be off
            // TODO: Refactor to use the ischecked instead of states, redo the logic if time permits, works but terrible implementation, checking if twice here

            Note to self: RadioGroup means that the buttons inside are exclusive
            Another Note to self: Radiobuttons arent able to be unselected....
             */
            // Get location and display on the text for now



            //binding.debugTextViewCurrent.text = "Current latitude: ${currentLatitude}\nCurrent longitude: ${currentLongitude}"

            //Might have to just bite the bullet and pull the data from the text fields


            /* TODO: NEED TO DO THE CALL TO CALCULATE THE AND DISPLAY THE DISTANCE
                "Distance was 1.56km, this is more than the

             */
            // need to do the logic to calculate the distance and whatnot

            if ((binding.switch1.isChecked and binding.LED1CheckBox.isChecked)
                    or (binding.switch2.isChecked and binding.LED2CheckBox.isChecked)
                    or (binding.switch3.isChecked and binding.LED3CheckBox.isChecked)
                    or (binding.switch4.isChecked and binding.LED4CheckBox.isChecked)){
                // GET THE LIST OF DEVICES TO BE SWITCHED OFF AND SWITCH THE DEVICES OFF
                var ledStringList = mutableListOf<Int>()

                if ((stateLED1checkBox == 1) and (binding.switch1.isChecked == true)) {
                    ledStringList.add(1)
                    binding.switch1.isChecked = false
                }
                if ((stateLED2checkBox == 1) and (binding.switch2.isChecked == true)) {
                    ledStringList.add(2)
                    binding.switch2.isChecked = false
                }
                if ((stateLED3checkBox == 1) and (binding.switch3.isChecked == true)) {
                    ledStringList.add(3)
                    binding.switch3.isChecked = false
                }
                if ((stateLED4checkBox == 1) and (binding.switch4.isChecked == true)) {
                    ledStringList.add(4)
                    binding.switch4.isChecked = false
                }


                var homeLocation = binding.homeCoordinatesTextView.text
                var trimString = homeLocation.toString().replace("Home Location set at:\n","")
                var splitString = trimString.split(", ")

                var homeLatitude = splitString[0]
                var homeLongitude = splitString[1]

                //binding.debugTextViewHome.text = "Home latitude: ${homeLatitude}\nHome Longitude: ${homeLongitude}"
                //Thread.sleep(10000)



                var testLocation = binding.gpsLocationTextView.text
                var testString = testLocation.toString().replace("Current location:\n", "")
                splitString = testString.split(", ")

                var currentLatitude = splitString[0]
                var currentLongitude = splitString[1]


                //binding.debugTextViewCurrent.text = "Current latitude: ${currentLatitude}\nCurrent Longitude: ${currentLongitude}"


                var distance = calculateDistanceUsingSphericalModel(homeLatitude.toDouble(), currentLatitude.toDouble(), homeLongitude.toDouble(), currentLongitude.toDouble())

                binding.distanceTextView.text = distance.toString()

                if(distance<distanceRadius){
                    binding.textView5.text = "Device is inside of zone"
                }
                else{
                    binding.textView5.text = "Device is outside of zone, switching off devices"
                }


                // Make String for Notification
                var notificationString = "Smart Home has turned the following devices off: \n"
                for (i in ledStringList) {
                    notificationString += "LED${i}\n"
                }


                /*

                */
                //var distanceString = distance.toString()
                //binding.distanceTextView.text = "Distance is ${distanceString}"




                // PUSH NOTIFICATION
                sendNotification(notificationString)
            }
            /*
           Upon exceeding distance from home, set all the lights/devices off
           Easy way is just to switch off the items in the app and send a post request with parameters = 0
           Then set all the switches to off

           Have to figure out a way of showing/presenting the implementation as well

            */

            /*
            binding.textViewReset.text = "YOLO"
            binding.switch1.isChecked = false // setChecked uses the bool state to determine
             */
            // checked or unchecked
            // huh apparently .ischecked is better?

        }
        binding.setHomeButton.setOnClickListener{

            // TODO: NEED TO REFACTOR TO INCLUDE NO INPUT, IF THERE IS NO INPUT, THERE WILL BE AN ERROR
            var latitude = binding.latitudeInput.text
            var longitude = binding.longitudeInput.text
            binding.homeCoordinatesTextView.text = "Home Location set at:\n${latitude}, ${longitude}"
            //homeLatitude = latitude.toString().toDouble()
            //homeLongitude = longitude.toString().toDouble()
            fetchLocation()

        }


        //binding.seekBar.setOnSeekBarChangeListener()
        // ANALOG BARS

        //TODO: Convert Hardcoded text to strings


        //TODO: Vertical Scrolling for Buttons, have a bunch of stuff, alternatively create more layouts


        /*
        TODO: Analog Bars
            Need implementation of the reading on Android and Raspberry Pi
            Probably as a bonus after finishing the GPS functionality, that seems to be the key feature of the system

         */
        /*
        TODO: Figure out how to present GPS system functionality, calculate that device has left the zone
            GPS is 1km out, since technically the Earth is a sphere, how to use longitude and latitude
            Ideas right now:
                1 box for the latitude
                1 box for the longitude


        */


    }

    private fun fetchLocation() {
        if(binding.enableGPSSwitch.isChecked){
            val task = fusedLocationProviderClient.lastLocation
            if (ActivityCompat.checkSelfPermission(
                    this,
                    android.Manifest.permission.ACCESS_FINE_LOCATION
                ) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(
                    this,
                    android.Manifest.permission.ACCESS_COARSE_LOCATION
                ) != PackageManager.PERMISSION_GRANTED
            ) {
                ActivityCompat.requestPermissions(
                    this,
                    arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION),
                    101
                )

            }
            task.addOnSuccessListener {
                if (it != null) {
                    //currentLatitude = it.latitude
                    //currentLongitude = it.longitude
                    binding.gpsLocationTextView.text = "Current location:\n${it.latitude}, ${it.longitude}"
                    /*
                    currentLatitude = it.latitude.toString()
                    currentLongitude = it.longitude.toString()

                     */
                }
            }
        }

    }

    private fun postRequest() {

        val queue = Volley.newRequestQueue(this)

        val url =
            "https://script.google.com/macros/s/AKfycby5NUCX_vYyPgKz6BL0h5jhhOst-AsrgpBirHwFb9eTq9BpO0NbBOIOiElaTfpXbhd2TA/exec?"

        val newURL =
            url + "LED1State=" + stateLED1.toString() + "&LED2State=" + stateLED2.toString() + "&LED3State=" + stateLED3.toString() + "&LED4State=" + stateLED4.toString()

        val stringRequest = StringRequest(
            Request.Method.POST, newURL,
            Response.Listener<String> { response ->
                val numberOfCharacters = response.length


            },
            Response.ErrorListener {})

        // Add the request to the RequestQueue.
        queue.add(stringRequest)

    }

    private fun createNotificationChannel() {
        // Create the NotificationChannel, but only on API 26+ because
        // the NotificationChannel class is new and not in the support library
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val name = "Testing Notification Name"
            val descriptionText = "Lorem Ipsum"
            val importance = NotificationManager.IMPORTANCE_DEFAULT
            val channel = NotificationChannel(CHANNEL_ID, name, importance).apply {
                description = descriptionText
            }
            // Register the channel with the system
            val notificationManager: NotificationManager =
                getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
            notificationManager.createNotificationChannel(channel)
        }
    }

    private fun sendNotification(notificationString: String) {

        val intent = Intent(this, MainActivity::class.java).apply {
            flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
        }
        val pendingIntent: PendingIntent = PendingIntent.getActivity(this, 0, intent, 0)

        val bitmap = BitmapFactory.decodeResource(
            applicationContext.resources,
            R.drawable.ic_launcher_foreground
        )
        val bitmapLargeIcon = BitmapFactory.decodeResource(
            applicationContext.resources,
            R.drawable.ic_launcher_foreground
        )

        val builder = NotificationCompat.Builder(this, CHANNEL_ID)
            .setSmallIcon(R.drawable.ic_launcher_foreground)
            .setContentTitle("Smart Home GPS Feature")
            .setContentText("Smart Home has turned off your selected devices")
            .setLargeIcon(bitmapLargeIcon)
            //.setStyle(NotificationCompat.BigPictureStyle().bigPicture(bitmap))
            // Idea here is to have the bigtext display the selected devices turned off
            .setStyle(NotificationCompat.BigTextStyle().bigText(notificationString))

            .setContentIntent(pendingIntent)
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)

        with(NotificationManagerCompat.from(this)) {
            notify(notificationId, builder.build())
        }

    }

    private fun calculateDistanceUsingSphericalModel(
        latitude1: Double, latitude2: Double, longitude1: Double, longitude2: Double): Double {

        // algo from: https://stackoverflow.com/a/21623206

        var p = Math.PI/180
        var a = 0.5 - cos((latitude2-latitude1)*p)/2 + cos(latitude1*p) * cos(latitude2*p) * (1-cos((longitude2-longitude1)*p))/2

        return  12742 * kotlin.math.asin(kotlin.math.sqrt(a))
    }
}