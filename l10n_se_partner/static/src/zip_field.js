import { registry } from "@web/core/registry";
import { CharField, charField } from "@web/views/fields/char/char_field";

export class SeZipField extends CharField {
    get formattedValue() {
        const val = this.props.record.data[this.props.name] || "";
        const z = val.replace(/\s/g, "");
        if (/^\d{5}$/.test(z)) {
            return `${z.slice(0, 3)} ${z.slice(3)}`;
        }
        return super.formattedValue;
    }
}

export const seZipField = {
    ...charField,
    component: SeZipField,
    displayName: "SE Zip",
};

registry.category("fields").add("se_zip", seZipField);