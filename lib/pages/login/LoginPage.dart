import 'package:flutter/material.dart';
import 'package:pause_v1/server/Server.dart';
import 'package:pause_v1/services/screenSize.dart';
import 'package:provider/provider.dart';
import '../../APIs/FbAPI.dart';

// Login page TODO: Handle return to this page while logged in (i.e. through Android back button press)

class LoginPage extends StatelessWidget {
  @override
  Widget build (BuildContext context) {
    // Initialize ScreenSize if necessary
    if(!ScreenSize.initialized) {
      // ScreenSize
      ScreenSize().init(context);
    }

    return new Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'Login Page',
            ),
            RaisedButton(
              color: Color(0xff3b5998),
              shape:RoundedRectangleBorder(
                borderRadius: new BorderRadius.circular(18.0),
              ),
              textColor: Colors.white,
              onPressed: () {
                Server server = Provider.of<Server>(context, listen: false);
                FbAPI.loginToFB(server);

                // Register flow
                if (server.user.isNew) {
                  // TODO: Create troughout the app new-user tips
                  Navigator.pushNamed(context, '/Profile');
                  print('NewUser!');
                } else {
                  Navigator.pushNamed(context, '/Home');
                }

              },
              child: Text('Login with Facebook', style: TextStyle(fontSize: 20)),
            ),
          ],
        ),
      ),
    );

  }
}