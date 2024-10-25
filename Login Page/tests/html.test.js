const fs = require("fs");
const path = require("path");

describe("HTML Validation", () => {
  test("index.html should contain valid elements", () => {
    const htmlPath = path.join(__dirname, "../src/index.html");
    const htmlContent = fs.readFileSync(htmlPath, "utf-8");

    expect(htmlContent).toContain("<!DOCTYPE html>");
    expect(htmlContent).toContain("<title>");
    expect(htmlContent).toContain("<body>");
  });
});
