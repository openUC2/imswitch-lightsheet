import * as React from "react";
import { Button, Paper, Typography } from "@mui/material";

/**
 * A *very* small React component – counts clicks.
 * The host passes `hostIP` and `hostPort` as props; we just show them.
 */
export default function LightsheetWidget({ hostIP, hostPort }) {
  const [cnt, setCnt] = React.useState(0);

  return (
    <Paper sx={{ p: 2, maxWidth: 320 }}>
      <Typography variant="h6" gutterBottom>
        Hello from the Lightsheet remote 🎉
      </Typography>

      <Typography variant="body2">
        Host API: <code>{hostIP}:{hostPort}</code>
      </Typography>

      <Button
        sx={{ mt: 2 }}
        variant="contained"
        onClick={() => setCnt((c) => c + 1)}
      >
        Click me ({cnt})
      </Button>
    </Paper>
  );
}
